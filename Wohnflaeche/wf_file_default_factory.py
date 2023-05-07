import pathlib

from Domain.General import GLand
from Domain.Wohnflaeche import WFFileFactory, WFFile


class WFFileDefaultFactory(WFFileFactory):
    def __init__(self, path: pathlib.Path):
        self.__path = path

    def create(self, laender: list[GLand]) -> WFFile:
        return WFFile(self.__path / 'Wohnflaeche.xlsx', laender)
