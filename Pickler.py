import pathlib

import Bevoelkerung
import Domain.General
import Energiebilanz
import General
import Nutzenergieanalyse
import Processor


def setup_general_data(g_laender_factory: Domain.General.GLaenderFactory):
    g_sektoren_factory = General.GSektorenDefaultFactory()
    g_bereiche_factory = General.GBereicheDefaultFactory()
    g_energietraeger_klassen_factory = General.GEnergietraegerKlassenDefaultFactory()
    g_energietraeger_factory = General.GEnergietraegerDefaultFactory()
    g_data_factory = General.GDataFactory(g_laender_factory, g_sektoren_factory, g_bereiche_factory,
                                          g_energietraeger_klassen_factory, g_energietraeger_factory)
    g_data = g_data_factory.create()
    return g_data


def setup_nea_new_factory(g_data: Domain.General.GData):
    nea_files_factory = Nutzenergieanalyse.NEAFilesDefaultFactory(pathlib.Path('Data/Nutzenergieanalyse'),
                                                                  g_data.laender)
    nea_abschnitte_factory = Nutzenergieanalyse.NEAAbschnitteSimpleFactory()
    nea_data_factory = Nutzenergieanalyse.NEADataNewFactory(nea_files_factory, nea_abschnitte_factory)
    return nea_data_factory


def setup_nea_pickle_factory():
    nea_data_factory = Nutzenergieanalyse.NEADataPickleFactory(pathlib.Path('Data/Serialization'))
    return nea_data_factory


def setup_nea_klassen_factory(g_data: Domain.General.GData):
    nea_factory = setup_nea_new_factory(g_data)
    klassen_factory = Nutzenergieanalyse.NEADataETKlassenFactory(nea_factory)
    return klassen_factory


def setup_nea_processor(g_data: Domain.General.GData):
    nea_data_factory = setup_nea_new_factory(g_data)
    factory = Processor.NEAProcessorFactory(nea_data_factory)
    return factory.create(g_data)


def setup_eb_new_factory(g_data: Domain.General.GData):
    eb_files_factory = Energiebilanz.EBFilesDefaultFactory(pathlib.Path('Data/Energiebilanz'), g_data.laender)
    eb_data_factory = Energiebilanz.EBDataNewFactory(eb_files_factory)
    return eb_data_factory


def setup_eb_pickle_factory():
    eb_data_factory = Energiebilanz.EBDataPickleFactory(pathlib.Path('Data/Serialization'))
    return eb_data_factory


def setup_eb_processor(g_data: Domain.General.GData):
    eb_data_factory = setup_eb_new_factory(g_data)

    factory = Processor.EBProcessorFactory(eb_data_factory)

    return factory.create(g_data)


def setup_b_new_factory(g_data: Domain.General.GData):
    b_file_factory = Bevoelkerung.BFileDefaultFactory(pathlib.Path('Data/Bevoelkerung'))
    b_file = b_file_factory.create(list(g_data.laender.values()))
    b_data_factory = Bevoelkerung.BDataNewFactory(b_file)
    return b_data_factory


def setup_b_pickle_factory(g_data: Domain.General.GData):
    b_data_factory = Bevoelkerung.BDataPickleFactory(pathlib.Path('Data/Serialization'), list(g_data.laender.values()))
    return b_data_factory


def setup_b_processor(g_data: Domain.General.GData):
    b_data_factory = setup_b_new_factory(g_data)

    factory = Processor.BProcessorFactory(b_data_factory, list(g_data.laender.values()))

    return factory.create()


def pickle_all(g_laender_factory: Domain.General.GLaenderFactory):
    g_sektoren_factory = General.GSektorenDefaultFactory()
    g_bereiche_factory = General.GBereicheSimpleFactory()
    g_energietraeger_klassen_factory = General.GEnergietraegerKlassenSimpleFactory()
    g_energietraeger_factory = General.GEnergietraegerSimpleFactory()
    g_data_factory = General.GDataFactory(g_laender_factory, g_sektoren_factory, g_bereiche_factory,
                                          g_energietraeger_klassen_factory, g_energietraeger_factory)
    g_data = g_data_factory.create()

    nea_processor = setup_nea_processor(g_data)
    nea_processor.run_pickle_serialization()
    #nea_processor.run_validation()

    eb_processor = setup_eb_processor(g_data)
    eb_processor.run_pickle_serialization()

    #b_processor = setup_b_processor(g_data)
    #b_processor.run_pickle_serialization()
