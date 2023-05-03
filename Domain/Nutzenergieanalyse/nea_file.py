import pathlib
from dataclasses import dataclass

from .nea_land import NEALand


@dataclass
class NEAFile:
    path: pathlib.Path
    land: NEALand
