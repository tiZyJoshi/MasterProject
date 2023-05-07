import pathlib

from Domain.Bevoelkerung import BFileFactory, BFile
from Domain.General import GLand


class BFileDefaultFactory(BFileFactory):
    def __init__(self, path: pathlib.Path):
        self.__path = path

    def create(self, laender: list[GLand]) -> BFile:
        return BFile(self.__path / 'Bevoelkerung.xlsx', laender)
