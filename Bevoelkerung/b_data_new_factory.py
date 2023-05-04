from Domain.Bevoelkerung import BFile, BData, BDataFactory
from Domain.General import GLand

import pandas as pd


class BDataNewFactory(BDataFactory):
    def __init__(self, file: BFile):
        self.__file = file

    def create(self, laender: list[GLand]) -> BData:
        with pd.ExcelFile(self.__file.path) as xls:
            data = pd.read_excel(xls, header=0, index_col=0)
            data.index = pd.PeriodIndex(data.index, freq='A')
            return BData(laender, {land: data[land.name] for land in laender})
