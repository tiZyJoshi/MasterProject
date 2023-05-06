import pandas as pd

from Domain.General import GData, GBereich
from Domain.Nutzenergieanalyse import NEAJahr, NEAAbschnitt, NEASektor, NEABereich, NEAEnergietraeger
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
        return pd.Series((data[jahr][bereich.name] for jahr in jahre), index, name=et.entspricht.name)

    def __create_dataframe(self, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich,
                           abschnitt_dictionary: NEAAbschnittDictionary) -> pd.DataFrame:
        return pd.concat(
            (self.__create_series(abschnitt.jahre, sektor, bereich, et, abschnitt_dictionary) for et in
             abschnitt.energietraeger), axis=1)

    @staticmethod
    def __to_g_bereiche(bereich: GBereich, data: list[tuple[NEABereich, pd.DataFrame]]):
        return sum([df for nea_bereich, df in data if nea_bereich.gehoert_zu == bereich])

    def __create_bereich_dataframes(self, abschnitt: NEAAbschnitt, sektor: NEASektor,
                                    abschnitt_dictionary: NEAAbschnittDictionary, g_data: GData) \
            -> dict[GBereich, pd.DataFrame]:
        data = list([(bereich, self.__create_dataframe(abschnitt, sektor, bereich, abschnitt_dictionary))
                     for bereich in (sektor.bereiche + sektor.add_bereiche)])
        return {bereich: self.__to_g_bereiche(bereich, data) for bereich in g_data.bereiche.values()}

    def create(self, abschnitt: NEAAbschnitt, abschnitt_dictionary: NEAAbschnittDictionary,
               g_data: GData) -> NEAAbschnittDataframes:
        return {sektor.entspricht: self.__create_bereich_dataframes(abschnitt, sektor, abschnitt_dictionary, g_data) for
                sektor in abschnitt.sektoren}
