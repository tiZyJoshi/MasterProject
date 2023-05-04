import pathlib

import pandas as pd

from Domain.Energiebilanz import EBLand, EBSektor, EBEnergietraeger, EBData, EBDataFactory
from .eb_pickle_path_factory import EBPicklePathFactory


class EBDataPickleFactory(EBDataFactory):
    def __init__(self, path: pathlib.Path, laender: list[EBLand]):
        self.__laender = laender
        self.__path_factory = EBPicklePathFactory(path)

    def __read_eb_pickle(self, land: EBLand, sektor: EBSektor):
        ser_path = self.__path_factory.create(land, sektor)
        return pd.read_pickle(ser_path)

    def __restore_eb_dataframes(self, land: EBLand, sektoren: list[EBSektor]):
        return {sektor: self.__read_eb_pickle(land, sektor) for sektor in sektoren}

    def create(self, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]) -> EBData:
        return EBData(self.__laender, energietraeger, sektoren, {
            land: self.__restore_eb_dataframes(land, sektoren) for land in self.__laender})
