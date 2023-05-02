import pathlib

import pandas as pd

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_data import NEAData
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEAExcelSerializer:
    def __init__(self, path: pathlib.Path, laender: list[NEALand],
                 abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor], bereiche: list[NEABereich]):
        self.__path = path
        self.__laender = laender
        self.__abschnitte = abschnitte
        self.__sektoren = sektoren
        self.__bereiche = bereiche

    def run(self, data: NEAData):
        filename = self.__path / 'nutzenergieanalyse.xlsx'
        with pd.ExcelWriter(filename) as writer:
            for land in self.__laender:
                for abschnitt in self.__abschnitte:
                    for sektor in self.__sektoren:
                        for bereich in self.__bereiche:
                            local_df = data.get(land, abschnitt, sektor, bereich).copy()
                            local_df.index = pd.Index((period.year for period in local_df.index),
                                                      name=local_df.index.name)
                            local_df = local_df.swapaxes("index", "columns")
                            local_df.to_excel(writer, f'{land.name[0:9]}-{sektor.name[0:9]}-{bereich.name[0:9]}')
