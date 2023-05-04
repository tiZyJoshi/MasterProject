from dataclasses import dataclass


@dataclass
class NEABereich:
    name: str
    name_bereinigt: str

    def __hash__(self):
        return hash(self.name)

