from Domain.Hauptwohnsitze import HWSFile, HWSData, HWSDataFactory
from Domain.General import GLand

import pandas as pd


class HWSDataNewFactory(HWSDataFactory):
    def __init__(self, file: HWSFile):
        self.__file = file

    def create(self, laender: list[GLand]) -> HWSData:
        with pd.ExcelFile(self.__file.path) as xls:
            data = pd.read_excel(xls, header=0, index_col=0)
            data.index = pd.PeriodIndex(data.index, freq='A')
            return HWSData(laender, {land: data[land.name] for land in laender})
