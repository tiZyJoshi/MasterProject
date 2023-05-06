import pathlib

import pandas as pd

from Domain.General import GLand, GSektor
from Domain.Energiebilanz import EBLand, EBSektor, EBEnergietraeger, EBData, EBDataFactory
from .eb_pickle_path_factory import EBPicklePathFactory


class EBDataPickleFactory(EBDataFactory):
    def __init__(self, path: pathlib.Path, laender: list[EBLand]):
        self.__laender = laender
        self.__path_factory = EBPicklePathFactory(path)

    def __read_eb_pickle(self, land: GLand, sektor: GSektor):
        ser_path = self.__path_factory.create(land, sektor)
        return pd.read_pickle(ser_path)

    def __restore_eb_dataframes(self, land: GLand, sektoren: list[EBSektor]):
        return {sektor: self.__read_eb_pickle(land, sektor.entspricht) for sektor in sektoren}

    def create(self, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]) -> EBData:
        return EBData(
            {land.entspricht: self.__restore_eb_dataframes(land.entspricht, sektoren) for land in self.__laender})
