import pathlib

import pandas as pd

from .b_pickle_path_factory import BPicklePathFactory
from Domain.Bevoelkerung import BDataFactory, BData
from Domain.General import GLand


class BDataPickleFactory(BDataFactory):
    def __init__(self, path: pathlib.Path, laender: list[GLand]):
        self.__laender = laender
        self.__path_factory = BPicklePathFactory(path)

    def __read_b_pickle(self, land: GLand):
        ser_path = self.__path_factory.create(land)
        return pd.read_pickle(ser_path)

    def create(self, laender: list[GLand]) -> BData:
        return BData(self.__laender, {land: self.__read_b_pickle(land) for land in self.__laender})
