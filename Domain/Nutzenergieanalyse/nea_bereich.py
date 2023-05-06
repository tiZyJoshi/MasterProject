from dataclasses import dataclass

from .nea_bereich_klasse import NEABereichKlasse

@dataclass
class NEABereich:
    name: str
    name_bereinigt: str
    klasse: NEABereichKlasse

    def __hash__(self):
        return hash(self.name)

