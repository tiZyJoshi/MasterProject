import pathlib

from Domain.Nutzenergieanalyse import NEAAbschnitt, NEALand, NEASektor, NEABereich


class NEAPicklePathFactory:
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

    def create(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor, bereich: NEABereich) -> pathlib.Path:
        nea_serialization_folder = self.__create_nea_serialization_folder(land, abschnitt)
        sektor_folder = nea_serialization_folder / sektor.name
        path = sektor_folder / f'{bereich.name}.pkl'
        return path
