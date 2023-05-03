from dataclasses import dataclass

from .nea_energietraeger import NEAEnergietraeger
from .nea_jahr import NEAJahr


@dataclass
class NEAAbschnitt:
    name: str
    jahre: list[NEAJahr]
    energietraeger: list[NEAEnergietraeger]

    def __hash__(self):
        return hash(self.name)
