from dataclasses import dataclass

from General.GEnergietraegerKlasse import GEnergietraegerKlasse


@dataclass
class GEnergietraeger:
    name: str
    klasse: GEnergietraegerKlasse

    def __hash__(self):
        return hash(self.name)
