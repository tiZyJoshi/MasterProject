from dataclasses import dataclass

from General import GSektor


@dataclass
class NEASektor:
    name: str
    skiprows: int
    entspricht: GSektor

    def __hash__(self):
        return hash(self.name)
