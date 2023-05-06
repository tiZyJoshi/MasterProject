from dataclasses import dataclass


@dataclass
class NEABereichKlasse:
    name: str

    def __hash__(self):
        return hash(self.name)