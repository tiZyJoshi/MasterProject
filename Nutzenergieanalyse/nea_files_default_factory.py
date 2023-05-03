import pathlib
import re

from Domain.General import GLand
from Domain.Nutzenergieanalyse import NEALand, NEAFile, NEAFilesFactory


class NEAFilesDefaultFactory(NEAFilesFactory):
    def __init__(self, path: pathlib.Path, laender: dict[str, GLand]):
        self.__path = path
        self.__laender = laender

    def __generate_nea_files(self):
        for file in self.__path.glob('*.xlsx'):
            parts = re.split('_|\.', file.name)
            land = parts[1]
            if land not in self.__laender.keys():
                continue
            nea_land = NEALand(land, self.__laender[land])
            yield NEAFile(file, nea_land)

    def create(self) -> list[NEAFile]:
        return list(self.__generate_nea_files())
