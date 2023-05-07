import pandas as pd

from Domain.Nutzenergieanalyse import NEAFile, NEAAbschnitt, NEAData, NEADataFactory, NEAFilesFactory, \
    NEAAbschnitteFactory
from Domain.General import GData, GSektor, GBereich

from .nea_abschnitt_data_factory import NEAAbschnittDataFactory
from .nea_abschnitt_dictionary_factory import NEAAbschnittDictionaryFactory
from .nea_abschnitt_dataframes_factory import NEAAbschnittDataframesFactory


class NEADataNewFactory(NEADataFactory):
    def __init__(self, files_factory: NEAFilesFactory, abschnitte_factory: NEAAbschnitteFactory):
        self.__files_factory = files_factory
        self.__abschnitte_factory = abschnitte_factory
        self.__data_factory = NEAAbschnittDataFactory()
        self.__dictionary_factory = NEAAbschnittDictionaryFactory()
        self.__dataframes_factory = NEAAbschnittDataframesFactory()

    def __load(self, file: NEAFile, abschnitt: NEAAbschnitt, g_data: GData):
        abschnitt_data_fields = self.__data_factory.create(file, abschnitt)
        abschnitt_dictionary = self.__dictionary_factory.create(abschnitt, abschnitt_data_fields)
        abschnitt_dataframes = self.__dataframes_factory.create(abschnitt, abschnitt_dictionary, g_data)
        return abschnitt_dataframes

    @staticmethod
    def __concat_abschnitte(g_data: GData, data: list[dict[GSektor, dict[GBereich, pd.DataFrame]]]):
        return {sektor: {bereich: pd.concat(list([d[sektor][bereich] for d in data])) for bereich in
                         g_data.bereiche.values()} for sektor in g_data.sektoren.values()}

    def create(self, g_data: GData) -> NEAData:
        files = self.__files_factory.create()
        abschnitte = self.__abschnitte_factory.create(g_data)
        return NEAData({file.land.entspricht: self.__concat_abschnitte(g_data, list(
            [self.__load(file, abschnitt, g_data) for abschnitt in abschnitte])) for file in files})
