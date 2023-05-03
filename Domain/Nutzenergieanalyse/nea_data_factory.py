from .nea_abschnitt import NEAAbschnitt
from .nea_sektor import NEASektor
from .nea_bereich import NEABereich
from .nea_data import NEAData


class NEADataFactory:
    def create(self, abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor],
               bereiche: list[NEABereich]) -> NEAData:
        pass
