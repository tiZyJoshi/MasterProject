from dataclasses import dataclass

from Domain.General import GSektor
from .nea_bereich import NEABereich


@dataclass
class NEASektor:
    name: str
    skiprows: int
    usecols: str
    bereiche: list[NEABereich]
    add_bereiche: list[NEABereich]
    entspricht: GSektor

    def __hash__(self):
        return hash(self.name)
