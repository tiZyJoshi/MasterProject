import pathlib

import pandas as pd

from Domain.Nutzenergieanalyse import NEAData, NEADataSerializer


class NEAExcelSerializer(NEADataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path = path

    def run(self, data: NEAData):
        filename = self.__path / 'nutzenergieanalyse.xlsx'
        with pd.ExcelWriter(filename) as writer:
            for land in data.laender:
                for abschnitt in data.abschnitte:
                    for sektor in data.sektoren:
                        for bereich in data.bereiche:
                            local_df = data.data[land][abschnitt][sektor][bereich].copy()
                            local_df.index = pd.Index((period.year for period in local_df.index),
                                                      name=local_df.index.name)
                            local_df = local_df.swapaxes("index", "columns")
                            local_df.to_excel(writer, f'{land.name[0:9]}-{sektor.name[0:9]}-{bereich.name[0:9]}')
