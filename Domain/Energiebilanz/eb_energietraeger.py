from dataclasses import dataclass

from Domain.General import GEnergietraeger


@dataclass
class EBEnergietraeger:
    name: str
    entspricht: GEnergietraeger

    def __hash__(self):
        return hash(self.name)
