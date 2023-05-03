from dataclasses import dataclass

from Domain.General import GSektor


@dataclass
class EBSektor:
    name: str
    entspricht: GSektor

    def __hash__(self):
        return hash(self.name)
