import pathlib

import pandas as pd

from Domain.General import GLand, GSektor, GData
from Domain.Energiebilanz import EBEnergietraeger, EBData, EBDataFactory
from .eb_pickle_path_factory import EBPicklePathFactory


class EBDataPickleFactory(EBDataFactory):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = EBPicklePathFactory(path)

    def __read_eb_pickle(self, land: GLand, sektor: GSektor):
        ser_path = self.__path_factory.create(land, sektor)
        return pd.read_pickle(ser_path)

    def __restore_eb_dataframes(self, land: GLand, g_data: GData):
        return {sektor: self.__read_eb_pickle(land, sektor) for sektor in g_data.sektoren.values()}

    def create(self, energietraeger: list[EBEnergietraeger], g_data: GData) -> EBData:
        return EBData(
            {land: self.__restore_eb_dataframes(land, g_data) for land in g_data.laender.values()})
