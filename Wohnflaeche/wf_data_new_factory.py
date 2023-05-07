from Domain.Wohnflaeche import WFFile, WFData, WFDataFactory
from Domain.General import GLand

import pandas as pd


class WFDataNewFactory(WFDataFactory):
    def __init__(self, file: WFFile):
        self.__file = file

    def create(self, laender: list[GLand]) -> WFData:
        with pd.ExcelFile(self.__file.path) as xls:
            data = pd.read_excel(xls, header=0, index_col=0)
            data.index = pd.PeriodIndex(data.index, freq='A')
            return WFData(laender, {land: data[land.name] for land in laender})
