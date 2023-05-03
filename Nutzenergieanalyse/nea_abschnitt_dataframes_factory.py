import pandas as pd

from Domain.Nutzenergieanalyse import NEAJahr, NEASektor, NEAEnergietraeger, NEABereich, NEAAbschnitt
from .nea_abschnitt_dataframes import NEAAbschnittDataframes
from .nea_abschnitt_dictionary import NEAAbschnittDictionary


class NEAAbschnittDataframesFactory:
    @staticmethod
    def __create_series_data(jahre: list[NEAJahr], sektor: NEASektor, et: NEAEnergietraeger,
                             abschnitt_dictionary: NEAAbschnittDictionary) -> dict[NEAJahr, pd.Series]:
        return {jahr: abschnitt_dictionary[jahr][sektor][et] for jahr in jahre}

    def __create_series(self, jahre: list[NEAJahr], sektor: NEASektor, bereich: NEABereich, et: NEAEnergietraeger,
                        abschnitt_dictionary: NEAAbschnittDictionary):
        data = self.__create_series_data(jahre, sektor, et, abschnitt_dictionary)
        index = pd.PeriodIndex((jahr.value for jahr in jahre), freq='A')
        return pd.Series((data[jahr][bereich.name] for jahr in data.keys()), index, name=et.name)

    def __create_dataframe(self, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich,
                           abschnitt_dictionary: NEAAbschnittDictionary) -> pd.DataFrame:
        return pd.concat(
            (self.__create_series(abschnitt.jahre, sektor, bereich, et, abschnitt_dictionary) for et in
             abschnitt.energietraeger), axis=1)

    def __create_bereich_dataframes(self, abschnitt: NEAAbschnitt, sektor: NEASektor, bereiche: list[NEABereich],
                                    abschnitt_dictionary: NEAAbschnittDictionary) -> dict[NEABereich, pd.DataFrame]:
        return {bereich: self.__create_dataframe(abschnitt, sektor, bereich, abschnitt_dictionary) for bereich in
                bereiche}

    def create(self, abschnitt: NEAAbschnitt, sektoren: list[NEASektor], bereiche: list[NEABereich],
               abschnitt_dictionary: NEAAbschnittDictionary) -> NEAAbschnittDataframes:
        return {sektor: self.__create_bereich_dataframes(abschnitt, sektor, bereiche, abschnitt_dictionary) for sektor
                in sektoren}
