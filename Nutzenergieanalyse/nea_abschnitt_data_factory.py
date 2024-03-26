import numpy as np
import pandas as pd

from Domain.Nutzenergieanalyse import NEAFile, NEAAbschnitt
from .nea_datafield import NEADataField


class NEAAbschnittDataFactory:
    @staticmethod
    def __load(file: NEAFile, abschnitt: NEAAbschnitt):
        print(f'Starting {file.land.name}')
        with pd.ExcelFile(file.path) as xls:
            for jahr in abschnitt.jahre:
                print(f'Starting {jahr}')
                if jahr.sheet not in xls.sheet_names:
                    print(f'{jahr} missing')
                    continue

                for sektor in abschnitt.sektoren:
                    raw_data = pd.read_excel(xls, sheet_name=jahr.sheet, header=0, index_col=0, usecols=sektor.usecols,
                                             skiprows=sektor.skiprows, nrows=22)
                    x, y = raw_data.shape
                    if len(raw_data) == 0 or x == 0 or y == 0:
                        print(f'{jahr} empty')
                        continue
                    local_df = raw_data[1:].fillna(0)
                    local_df.rename(index={'Erdgas (inkl. Mischgas)': 'Erdgas'}, inplace=True)
                    local_df.rename(index={'Brennholz': 'Scheitholz'}, inplace=True)
                    local_df.index = pd.Index((s.strip() for s in local_df.index), name=local_df.index.name)
                    local_df = local_df.filter(items=list(et.name for et in abschnitt.energietraeger),
                                               axis=0).transpose()
                    local_df.index = pd.Index((b.name for b in sektor.bereiche), name=local_df.index.name)

                    local_df = local_df.transpose()
                    for add_bereich in sektor.add_bereiche:
                        local_df[add_bereich.name] = np.nan
                    local_df = local_df.transpose()

                    for energietraeger in abschnitt.energietraeger:
                        series = local_df[energietraeger.name]
                        yield NEADataField(jahr, sektor, energietraeger, series)

    def create(self, file: NEAFile, abschnitt: NEAAbschnitt) -> list[NEADataField]:
        return list(self.__load(file, abschnitt))
