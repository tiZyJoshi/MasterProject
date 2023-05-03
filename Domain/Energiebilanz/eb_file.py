import pathlib
from dataclasses import dataclass

from .eb_land import EBLand


@dataclass
class EBFile:
    path: pathlib.Path
    typ: str
    land: EBLand
