import pathlib

from .eb_land import EBLand
from .eb_sektor import EBSektor


class EBSerializationFolderFactory:
    def create(self, land: EBLand, sektor: EBSektor) -> pathlib.Path:
        pass
