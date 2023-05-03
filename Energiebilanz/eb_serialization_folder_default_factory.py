import pathlib

from Domain.Energiebilanz import EBLand, EBSektor
from Domain.Energiebilanz.eb_serialization_folder_factory import EBSerializationFolderFactory


class EBSerializationFolderDefaultFactory(EBSerializationFolderFactory):
    def __init__(self, path: pathlib.Path):
        self.__path = path
        self.__folder_name = 'Energiebilanz'

    def __create_folder_name(self):
        return f'{self.__folder_name}'

    def __create_land_serialization_folder(self, land: EBLand):
        folder = self.__path / land.name
        return folder

    def __create_eb_serialization_folder(self, land: EBLand):
        land_serialization_folder = self.__create_land_serialization_folder(land)
        folder = land_serialization_folder / self.__folder_name
        return folder

    def create(self, land: EBLand, sektor: EBSektor) -> pathlib.Path:
        nea_serialization_folder = self.__create_eb_serialization_folder(land)
        folder = nea_serialization_folder / sektor.name
        return folder
