from dataclasses import dataclass

from .g_energietraeger_klasse import GEnergietraegerKlasse


@dataclass
class GEnergietraeger:
    name: str
    klasse: GEnergietraegerKlasse

    def __hash__(self):
        return hash(self.name)
