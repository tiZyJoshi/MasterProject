import pathlib

from Domain.General import GLand
from Domain.Hauptwohnsitze import HWSFileFactory, HWSFile


class HWSFileDefaultFactory(HWSFileFactory):
    def __init__(self, path: pathlib.Path):
        self.__path = path

    def create(self, laender: list[GLand]) -> HWSFile:
        return HWSFile(self.__path / 'Hauptwohnsitze.xlsx', laender)
