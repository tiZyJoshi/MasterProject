import pathlib

import pandas as pd

from Domain.General import GLand
from Domain.Wohnflaeche import WFDataFactory, WFData
from .wf_pickle_path_factory import WFPicklePathFactory


class WFDataPickleFactory(WFDataFactory):
    def __init__(self, path: pathlib.Path, laender: list[GLand]):
        self.__laender = laender
        self.__path_factory = WFPicklePathFactory(path)

    def __read_b_pickle(self, land: GLand):
        ser_path = self.__path_factory.create(land)
        return pd.read_pickle(ser_path)

    def create(self, laender: list[GLand]) -> WFData:
        return WFData(self.__laender, {land: self.__read_b_pickle(land) for land in self.__laender})
