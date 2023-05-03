# This is a sample Python script.
import pathlib

import Domain.General
import General
import Nutzenergieanalyse
import Processor
from Domain.General import GLand, GEnergietraeger, GEnergietraegerKlasse, GSektor
from Domain.Nutzenergieanalyse import NEALand, NEAAbschnitt, NEASektor, NEABereich, NEATyp


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def setup_processor():
    g_laender_factory = General.GBundeslaenderFactory()
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
    nea_abschnitt_data_factory = Nutzenergieanalyse.NEAAbschnittDataDefaultFactory()
    nea_abschnitt_dictionary_factory = Nutzenergieanalyse.NEAAbschnittDictionaryDefaultFactory()
    nea_abschnitt_dataframes_factory = Nutzenergieanalyse.NEAAbschnittDataframesDefaultFactory()
    nea_data_factory = Nutzenergieanalyse.NEADataNewFactory(nea_files_factory, nea_abschnitt_data_factory,
                                                            nea_abschnitt_dictionary_factory,
                                                            nea_abschnitt_dataframes_factory)

    factory = Processor.ProcessorFactory(g_data_factory, nea_abschnitte_factory, nea_sektoren_factory,
                                         nea_bereiche_factory, nea_data_factory)

    return factory.create()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    processor = setup_processor()
    processor.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def plot_nea_differences(dataframes, bundeslaender: list[NEALand], oesterreich: list[NEALand],
                         abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor], bereiche: list[NEABereich]):
    # bl_sum = create_nea_laender_sum(dataframes, bundeslaender, abschnitte, sektoren, bereiche)
    # at_sum = create_nea_laender_sum(dataframes, oesterreich, abschnitte, sektoren, bereiche)
    # for abschnitt in abschnitte:
    #    (at_sum[abschnitt] - bl_sum[abschnitt]).plot()
    pass


def create_nea_typen():
    return [NEATyp('energiegesamtrechnungskonform', 'A:H')]


def create_nea_typen_ab_2005():
    return [NEATyp('energiegesamtrechnungskonform', 'A:H')]
