from .nea_abschnitt import NEAAbschnitt
from .nea_bereich import NEABereich
from .nea_file import NEAFile
from .nea_sektor import NEASektor
from .nea_datafield import NEADataField


class NEAAbschnittDataFactory:
    def create(self, file: NEAFile, abschnitt: NEAAbschnitt, sektoren: list[NEASektor], bereiche: list[NEABereich]) -> \
            list[NEADataField]:
        pass
