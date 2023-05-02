import pandas as pd

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_abschnitt_dataframes import NEAAbschnittDataframes
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_energietraeger import NEAEnergietraeger
from Nutzenergieanalyse.nea_jahr import NEAJahr
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEAAbschnittDictionary:
    def __init__(self, land: NEALand, sektoren: list[NEASektor], bereiche: list[NEABereich],
                 data: dict[NEAJahr, dict[NEASektor, dict[NEAEnergietraeger, pd.Series]]]):
        self.land = land
        self.__sektoren = sektoren
        self.__bereiche = bereiche
        self.__data = data

    def __create_series_data(self, jahre: list[NEAJahr], sektor: NEASektor, et: NEAEnergietraeger) -> dict[
        NEAJahr, pd.Series]:
        return {jahr: self.__data[jahr][sektor][et] for jahr in jahre}

    def __create_series(self, jahre: list[NEAJahr], sektor: NEASektor, bereich: NEABereich, et: NEAEnergietraeger):
        data = self.__create_series_data(jahre, sektor, et)
        index = pd.PeriodIndex((jahr.value for jahr in jahre), freq='A')
        return pd.Series((data[jahr][bereich.name] for jahr in data.keys()), index, name=et.name)

    def __create_dataframe(self, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich) -> pd.DataFrame:
        return pd.concat(
            (self.__create_series(abschnitt.jahre, sektor, bereich, et) for et in abschnitt.energietraeger), axis=1)

    def __create_bereich_dataframes(self, abschnitt: NEAAbschnitt, sektor: NEASektor) -> \
            dict[NEABereich, pd.DataFrame]:
        return {bereich: self.__create_dataframe(abschnitt, sektor, bereich) for bereich in self.__bereiche}

    def create_dataframes(self, abschnitt: NEAAbschnitt) -> NEAAbschnittDataframes:
        return NEAAbschnittDataframes(self.land, abschnitt,
                                      {sektor: self.__create_bereich_dataframes(abschnitt, sektor) for sektor in
                                       self.__sektoren})
