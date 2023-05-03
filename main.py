import pathlib

import Domain.General
import General
import Nutzenergieanalyse
import Processor


def setup_processor():
    g_laender_factory = General.GOesterreichFactory()
    g_sektoren_factory = General.GSektorenDefaultFactory()
    g_energietraeger_klassen_factory = General.GEnergietraegerKlassenDefaultFactory()
    g_energietraeger_klassen = g_energietraeger_klassen_factory.create()
    g_energietraeger_factory = General.GEnergietraegerDefaultFactory(g_energietraeger_klassen)
    g_data_factory = Domain.General.GDataFactory(g_laender_factory, g_sektoren_factory, g_energietraeger_factory)
    g_data = g_data_factory.create()

    nea_abschnitte_factory = Nutzenergieanalyse.NEAAbschnitteDefaultFactory(g_data.energietraeger)
    nea_sektoren_factory = Nutzenergieanalyse.NEASektorenDefaultFactory(g_data.sektoren)
    nea_bereiche_factory = Nutzenergieanalyse.NEABereicheDefaultFactory()
    nea_files_factory = Nutzenergieanalyse.NEAFilesDefaultFactory(pathlib.Path('Data/Nutzenergieanalyse'),
                                                                  g_data.laender)
    nea_data_factory = Nutzenergieanalyse.NEADataNewFactory(nea_files_factory)

    factory = Processor.ProcessorFactory(nea_abschnitte_factory, nea_sektoren_factory, nea_bereiche_factory,
                                         nea_data_factory)

    return factory.create()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processor = setup_processor()
    processor.run()
