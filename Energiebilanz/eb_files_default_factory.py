import pathlib
import re
import os

from Domain.General import GLand
from Domain.Energiebilanz import EBLand, EBFile, EBFilesFactory


class EBFilesDefaultFactory(EBFilesFactory):
    def __init__(self, path: pathlib.Path, laender: dict[str, GLand]):
        self.__path = path
        self.__laender = laender

    def __generate_files(self):
        for file in self.__path.glob('*.xlsx'):
            parts = re.split('_', os.path.splitext(file.name)[0])
            typ = parts[0]
            land = parts[1]
            if land not in self.__laender.keys():
                continue
            eb_land = EBLand(land, self.__laender[land])
            yield EBFile(file, typ, eb_land)

    def create(self) -> list[EBFile]:
        return list(self.__generate_files())
