import pandas as pd

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_data import NEAData
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor
from Nutzenergieanalyse.nea_serialization_folder_factory import NEASerializationFolderFactory


class NEAPickleDeserializer:
    def __init__(self, folder_factory: NEASerializationFolderFactory, laender: list[NEALand],
                 abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor], bereiche: list[NEABereich]):
        self.__laender = laender
        self.__abschnitte = abschnitte
        self.__sektoren = sektoren
        self.__bereiche = bereiche
        self.__folder_factory = folder_factory

    def __read_nea_pickle(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich):
        ser_path = self.__folder_factory.create(land, abschnitt, sektor)
        return pd.read_pickle(ser_path / f'{bereich.name}.pkl')

    def __restore_nea_sektor_dataframes(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor):
        return {bereich: self.__read_nea_pickle(land, abschnitt, sektor, bereich) for bereich in self.__bereiche}

    def __restore_nea_dataframes(self, land: NEALand, abschnitt: NEAAbschnitt):
        return {sektor: self.__restore_nea_sektor_dataframes(land, abschnitt, sektor) for sektor in self.__sektoren}

    def run(self) -> NEAData:
        return NEAData(self.__laender, self.__abschnitte, self.__sektoren, self.__bereiche, {
            land: {abschnitt: self.__restore_nea_dataframes(land, abschnitt) for abschnitt in self.__abschnitte} for
            land in self.__laender})
