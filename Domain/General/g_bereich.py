from dataclasses import dataclass


@dataclass
class GBereich:
    name: str

    def __hash__(self):
        return hash(type(self))
