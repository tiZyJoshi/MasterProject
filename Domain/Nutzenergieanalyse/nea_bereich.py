from dataclasses import dataclass

from Domain.General import GBereich


@dataclass
class NEABereich:
    name: str
    gehoert_zu: GBereich

    def __hash__(self):
        return hash(self.name)
