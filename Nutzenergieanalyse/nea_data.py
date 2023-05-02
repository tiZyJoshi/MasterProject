import pandas as pd

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEAData:
    def __init__(self, laender: list[NEALand], abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor],
                 bereiche: list[NEABereich],
                 data: dict[NEALand, dict[NEAAbschnitt, dict[NEASektor, dict[NEABereich, pd.DataFrame]]]]):
        self.laender = laender
        self.abschnitte = abschnitte
        self.sektoren = sektoren
        self.bereiche = bereiche
        self.__data = data

    def get(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich) -> pd.DataFrame:
        return self.__data[land][abschnitt][sektor][bereich]
