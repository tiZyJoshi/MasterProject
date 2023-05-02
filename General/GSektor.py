from dataclasses import dataclass


@dataclass
class GSektor:
    name: str

    def __hash__(self):
        return hash(self.name)
