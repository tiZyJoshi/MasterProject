import pathlib

import Bevoelkerung
import Domain.General
import Energiebilanz
import General
import Nutzenergieanalyse
import Processor


def setup_general_data():
    g_laender_factory = General.GBundeslaenderFactory()
    g_sektoren_factory = General.GSektorenDefaultFactory()
    g_energietraeger_klassen_factory = General.GEnergietraegerKlassenDefaultFactory()
    g_energietraeger_klassen = g_energietraeger_klassen_factory.create()
    g_energietraeger_factory = General.GEnergietraegerDefaultFactory(g_energietraeger_klassen)
    g_data_factory = Domain.General.GDataFactory(g_laender_factory, g_sektoren_factory, g_energietraeger_factory)
    g_data = g_data_factory.create()
    return g_data


def setup_nea_new_factory(g_data):
    nea_files_factory = Nutzenergieanalyse.NEAFilesDefaultFactory(pathlib.Path('Data/Nutzenergieanalyse'),
                                                                  g_data.laender)
    nea_data_factory = Nutzenergieanalyse.NEADataNewFactory(nea_files_factory)
    return nea_data_factory


def setup_nea_pickle_factory(g_data):
    nea_data_factory = Nutzenergieanalyse.NEADataPickleFactory(pathlib.Path('Data/Serialization'),
                                                               g_data.laender.values())
    return nea_data_factory


def setup_nea_processor():
    g_data = setup_general_data()

    nea_abschnitte_factory = Nutzenergieanalyse.NEAAbschnitteDefaultFactory(g_data.energietraeger)
    nea_sektoren_factory = Nutzenergieanalyse.NEASektorenDefaultFactory(g_data.sektoren)
    nea_bereiche_factory = Nutzenergieanalyse.NEABereicheDefaultFactory()

    nea_data_factory = setup_nea_pickle_factory(g_data)

    factory = Processor.NEAProcessorFactory(nea_abschnitte_factory, nea_sektoren_factory, nea_bereiche_factory,
                                            nea_data_factory)

    return factory.create()


def setup_eb_new_factory(g_data):
    eb_files_factory = Energiebilanz.EBFilesDefaultFactory(pathlib.Path('Data/Energiebilanz'), g_data.laender)
    eb_data_factory = Energiebilanz.EBDataNewFactory(eb_files_factory)
    return eb_data_factory


def setup_eb_pickle_factory(g_data):
    eb_data_factory = Energiebilanz.EBDataPickleFactory(pathlib.Path('Data/Serialization'), g_data.laender.values())
    return eb_data_factory


def setup_eb_processor():
    g_data = setup_general_data()

    eb_energietraeger_factory = Energiebilanz.EBEnergietraegerDefaultFactory(g_data.energietraeger)
    eb_sektoren_factory = Energiebilanz.EBSektorenDefaultFactory(g_data.sektoren)
    eb_data_factory = setup_eb_new_factory(g_data)

    factory = Processor.EBProcessorFactory(eb_energietraeger_factory, eb_sektoren_factory, eb_data_factory)

    return factory.create()


def setup_b_new_factory(g_data):
    b_file_factory = Bevoelkerung.BFileDefaultFactory(pathlib.Path('Data/Bevoelkerung'))
    b_file = b_file_factory.create(g_data.laender.values())
    b_data_factory = Bevoelkerung.BDataNewFactory(b_file)
    return b_data_factory


def setup_b_pickle_factory(g_data):
    b_data_factory = Bevoelkerung.BDataPickleFactory(pathlib.Path('Data/Serialization'), g_data.laender.values())
    return b_data_factory


def setup_b_processor():
    g_data = setup_general_data()

    b_data_factory = setup_b_new_factory(g_data)

    factory = Processor.BProcessorFactory(b_data_factory, g_data.laender.values())

    return factory.create()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processor = setup_eb_processor()
    processor.run_pickle_serialization()
