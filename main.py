import pathlib

import Domain.General
import Energiebilanz
import General
import Nutzenergieanalyse
import Processor


def setup_general_data():
    g_laender_factory = General.GOesterreichFactory()
    g_sektoren_factory = General.GSektorenDefaultFactory()
    g_energietraeger_klassen_factory = General.GEnergietraegerKlassenDefaultFactory()
    g_energietraeger_klassen = g_energietraeger_klassen_factory.create()
    g_energietraeger_factory = General.GEnergietraegerDefaultFactory(g_energietraeger_klassen)
    g_data_factory = Domain.General.GDataFactory(g_laender_factory, g_sektoren_factory, g_energietraeger_factory)
    g_data = g_data_factory.create()
    return g_data


def setup_nea_processor():
    g_data = setup_general_data()

    nea_abschnitte_factory = Nutzenergieanalyse.NEAAbschnitteDefaultFactory(g_data.energietraeger)
    nea_sektoren_factory = Nutzenergieanalyse.NEASektorenDefaultFactory(g_data.sektoren)
    nea_bereiche_factory = Nutzenergieanalyse.NEABereicheDefaultFactory()
    nea_files_factory = Nutzenergieanalyse.NEAFilesDefaultFactory(pathlib.Path('Data/Nutzenergieanalyse'),
                                                                  g_data.laender)
    nea_data_factory = Nutzenergieanalyse.NEADataNewFactory(nea_files_factory)

    factory = Processor.NEAProcessorFactory(nea_abschnitte_factory, nea_sektoren_factory, nea_bereiche_factory,
                                            nea_data_factory)

    return factory.create()


def setup_eb_processor():
    g_data = setup_general_data()

    eb_energietraeger_factory = Energiebilanz.EBEnergietraegerDefaultFactory(g_data.energietraeger)
    eb_sektoren_factory = Energiebilanz.EBSektorenDefaultFactory(g_data.sektoren)
    eb_files_factory = Energiebilanz.EBFilesDefaultFactory(pathlib.Path('Data/Energiebilanz'), g_data.laender)
    eb_data_factory = Energiebilanz.EBDataNewFactory(eb_files_factory)

    factory = Processor.EBProcessorFactory(eb_energietraeger_factory, eb_sektoren_factory, eb_data_factory)

    return factory.create()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processor = setup_eb_processor()
    processor.run()
