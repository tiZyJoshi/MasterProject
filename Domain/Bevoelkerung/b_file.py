import pathlib
from dataclasses import dataclass

from Domain.General import GLand


@dataclass
class BFile:
    path: pathlib.Path
    laender: list[GLand]
