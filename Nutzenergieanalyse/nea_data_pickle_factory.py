import pathlib

import pandas as pd

from Domain.Nutzenergieanalyse import NEALand, NEAAbschnitt, NEASektor, NEABereich, NEAData, NEADataFactory
from .nea_pickle_path_factory import NEAPicklePathFactory


class NEADataPickleFactory(NEADataFactory):
    def __init__(self, path: pathlib.Path, laender: list[NEALand]):
        self.__laender = laender
        self.__path_factory = NEAPicklePathFactory(path)

    def __read_nea_pickle(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich):
        ser_path = self.__path_factory.create(land, abschnitt, sektor, bereich)
        return pd.read_pickle(ser_path)

    def __restore_nea_sektor_dataframes(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor,
                                        bereiche: list[NEABereich]):
        return {bereich: self.__read_nea_pickle(land, abschnitt, sektor, bereich) for bereich in bereiche}

    def __restore_nea_dataframes(self, land: NEALand, abschnitt: NEAAbschnitt, sektoren: list[NEASektor],
                                 bereiche: list[NEABereich]):
        return {sektor: self.__restore_nea_sektor_dataframes(land, abschnitt, sektor, bereiche) for sektor in sektoren}

    def create(self, abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor],
               bereiche: list[NEABereich]) -> NEAData:
        return NEAData(self.__laender, abschnitte, sektoren, bereiche, {
            land: {abschnitt: self.__restore_nea_dataframes(land, abschnitt, sektoren, bereiche) for abschnitt in
                   abschnitte} for land in self.__laender})
