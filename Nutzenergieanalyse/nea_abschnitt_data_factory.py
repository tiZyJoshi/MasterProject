import pandas as pd

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_abschnitt_data import NEAAbschnittData
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_datafield import NEADataField
from Nutzenergieanalyse.nea_file import NEAFile
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEAAbschnittDataFactory:
    def __init__(self, sektoren: list[NEASektor], bereiche: list[NEABereich]):
        self.sektoren = sektoren
        self.bereiche = bereiche

    def __load(self, file: NEAFile, abschnitt: NEAAbschnitt):
        with pd.ExcelFile(file.path) as xls:
            for jahr in abschnitt.jahre:
                print(f'Starting {jahr}')
                if jahr.sheet not in xls.sheet_names:
                    print(f'{jahr} missing')
                    continue

                for sektor in self.sektoren:
                    raw_data = pd.read_excel(xls,
                                             sheet_name=jahr.sheet,
                                             header=0,
                                             index_col=0,
                                             usecols="A:H",
                                             skiprows=sektor.skiprows,
                                             nrows=22)
                    x, y = raw_data.shape
                    if len(raw_data) == 0 or x == 0 or y == 0:
                        print(f'{jahr} empty')
                        continue
                    local_df = raw_data[1:].fillna(0)
                    local_df.rename(index={'Erdgas (inkl. Mischgas)': 'Erdgas'}, inplace=True)
                    local_df.rename(index={'Brennholz': 'Scheitholz'}, inplace=True)
                    local_df.index = pd.Index((s.strip() for s in local_df.index), name=local_df.index.name)
                    local_df = local_df.filter(items=list(et.name for et in abschnitt.energietraeger), axis=0).swapaxes(
                        "index", "columns")
                    local_df.index = pd.Index((b.name for b in self.bereiche), name=local_df.index.name)
                    for energietraeger in abschnitt.energietraeger:
                        series = local_df[energietraeger.name]
                        yield NEADataField(jahr, sektor, energietraeger, series)

    def create(self, file: NEAFile, abschnitt: NEAAbschnitt) -> NEAAbschnittData:
        return NEAAbschnittData(file.land, self.sektoren, self.bereiche, list(self.__load(file, abschnitt)))
