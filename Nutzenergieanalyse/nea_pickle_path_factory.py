import pathlib

from Domain.General import GLand, GSektor, GBereich


class NEAPicklePathFactory:
    def __init__(self, path: pathlib.Path):
        self.__path = path
        self.__folder_name = 'Nutzenenergieanalyse'

    def __create_land_serialization_folder(self, land: GLand) -> pathlib.Path:
        folder = self.__path / land.name
        return folder

    def __create_nea_serialization_folder(self, land: GLand) -> pathlib.Path:
        land_serialization_folder = self.__create_land_serialization_folder(land)
        folder = land_serialization_folder / self.__folder_name
        return folder

    def create(self, land: GLand, sektor: GSektor, bereich: GBereich) -> pathlib.Path:
        nea_serialization_folder = self.__create_nea_serialization_folder(land)
        sektor_folder = nea_serialization_folder / sektor.name
        path = sektor_folder / f'{bereich.name}.pkl'
        return path
