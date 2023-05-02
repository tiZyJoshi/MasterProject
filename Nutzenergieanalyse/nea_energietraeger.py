from dataclasses import dataclass

from General import GEnergietraeger


@dataclass
class NEAEnergietraeger:
    name: str
    entspricht: GEnergietraeger

    def __hash__(self):
        return hash(self.name)
