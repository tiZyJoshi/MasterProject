from dataclasses import dataclass


@dataclass
class NEAJahr:
    sheet: str
    value: str

    def __hash__(self):
        return hash(self.value)
