from dataclasses import dataclass

from Domain.General import GLand


@dataclass
class NEALand:
    name: str
    entspricht: GLand

    def __hash__(self):
        return hash(self.name)
