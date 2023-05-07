import pathlib

from Domain.General import GLand


class HWSPicklePathFactory:
    def __init__(self, path: pathlib.Path):
        self.__path = path
        self.__folder_name = 'Hauptwohnsitze'
        self.__file_prefix = 'Hauptwohnsitze_'

    def __create_folder_name(self):
        return f'{self.__folder_name}'

    def __create_land_serialization_folder(self, land: GLand) -> pathlib.Path:
        folder = self.__path / land.name
        return folder

    def __create_hws_serialization_folder(self, land: GLand) -> pathlib.Path:
        land_serialization_folder = self.__create_land_serialization_folder(land)
        folder = land_serialization_folder / self.__folder_name
        return folder

    def create(self, land: GLand) -> pathlib.Path:
        b_serialization_folder = self.__create_hws_serialization_folder(land)
        path = b_serialization_folder / f'{self.__file_prefix}{land.name}.pkl'
        return path
