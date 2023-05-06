import pathlib

import pandas as pd

from Domain.General import GLand, GData, GSektor, GBereich
from Domain.Nutzenergieanalyse import NEAData, NEADataFactory
from .nea_pickle_path_factory import NEAPicklePathFactory


class NEADataPickleFactory(NEADataFactory):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = NEAPicklePathFactory(path)

    def __read_nea_pickle(self, land: GLand, sektor: GSektor, bereich: GBereich):
        ser_path = self.__path_factory.create(land, sektor, bereich)
        return pd.read_pickle(ser_path)

    def __restore_nea_sektor_dataframes(self, land: GLand, sektor: GSektor, g_data: GData):
        return {bereich: self.__read_nea_pickle(land, sektor, bereich) for bereich in g_data.bereiche.values()}

    def __restore_nea_dataframes(self, land: GLand, g_data: GData):
        return {sektor: self.__restore_nea_sektor_dataframes(land, sektor, g_data) for sektor in g_data.sektoren.values()}

    def create(self, g_data: GData) -> NEAData:
        return NEAData({land: self.__restore_nea_dataframes(land, g_data) for land in g_data.laender.values()})
