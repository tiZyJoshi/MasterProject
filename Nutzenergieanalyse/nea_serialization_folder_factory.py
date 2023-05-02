import pathlib

from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEASerializationFolderFactory:
    def __init__(self, path: pathlib.Path):
        self.__path = path
        self.__prefix = 'Nutzenenergieanalyse_'

    def __create_folder_name(self, abschnitt: NEAAbschnitt):
        return f'{self.__prefix}{abschnitt.name}'

    def __create_land_serialization_folder(self, land: NEALand):
        folder = self.__path / land.name
        return folder

    def __create_nea_serialization_folder(self, land: NEALand, abschnitt: NEAAbschnitt):
        land_serialization_folder = self.__create_land_serialization_folder(land)
        folder = land_serialization_folder / self.__create_folder_name(abschnitt)
        return folder

    def create(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor):
        nea_serialization_folder = self.__create_nea_serialization_folder(land, abschnitt)
        folder = nea_serialization_folder / sektor.name
        return folder
