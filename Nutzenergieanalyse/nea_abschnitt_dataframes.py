import pandas as pd

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEAAbschnittDataframes:
    def __init__(self, land: NEALand, abschnitt: NEAAbschnitt, data: dict[NEASektor, dict[NEABereich, pd.DataFrame]]):
        self.land = land
        self.abschnitt = abschnitt
        self.__data = data

    def get(self, sektor: NEASektor, bereich: NEABereich) -> pd.DataFrame:
        return self.__data[sektor][bereich]

    def get_enum(self, sektoren: list[NEASektor], bereiche: list[NEABereich]):
        for sektor in sektoren:
            for bereich in bereiche:
                yield sektor, bereich, self.get(sektor, bereich)
