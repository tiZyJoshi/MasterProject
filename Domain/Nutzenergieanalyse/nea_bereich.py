from dataclasses import dataclass


@dataclass
class NEABereich:
    name: str

    def __hash__(self):
        return hash(self.name)

