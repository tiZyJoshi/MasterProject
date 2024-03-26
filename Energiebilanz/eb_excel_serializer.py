import pathlib

import pandas as pd

from Domain.Energiebilanz import EBData, EBDataSerializer


class EBExcelSerializer(EBDataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path = path

    def run(self, data: EBData):
        filename = self.__path / 'energiebilanz.xlsx'
        with pd.ExcelWriter(filename) as writer:
            for land in data.data.keys():
                for sektor in data.data[land].keys():
                    local_df = data.data[land][sektor].copy()
                    local_df.index = pd.Index((period.year for period in local_df.index), name=local_df.index.name)
                    local_df = local_df.transpose()
                    local_df.to_excel(writer, f'{land.name[0:14]}-{sektor.name[0:14]}')
