import pathlib
import re

from General.GLand import GLand
from Nutzenergieanalyse.nea_file import NEAFile
from Nutzenergieanalyse.nea_files import NEAFiles
from Nutzenergieanalyse.nea_land import NEALand


class NEAFilesFactory:
    def __init__(self, path: pathlib.Path):
        self.path = path

    def __generate_nea_files(self, laender: dict[str, GLand]):
        for file in self.path.glob('*.xlsx'):
            parts = re.split('_|\.', file.name)
            land = NEALand(parts[1], laender[parts[1]])
            yield NEAFile(file, land)

    def create(self, laender: dict[str, GLand]) -> NEAFiles:
        return NEAFiles(list(self.__generate_nea_files(laender)))
