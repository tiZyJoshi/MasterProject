from dataclasses import dataclass

from .nea_energietraeger import NEAEnergietraeger
from .nea_jahr import NEAJahr
from .nea_sektor import NEASektor


@dataclass
class NEAAbschnitt:
    name: str
    jahre: list[NEAJahr]
    sektoren: list[NEASektor]
    energietraeger: list[NEAEnergietraeger]

    def __hash__(self):
        return hash(self.name)
