from .nea_abschnitt import NEAAbschnitt
from .nea_sektor import NEASektor
from .nea_bereich import NEABereich
from .nea_abschnitt_dataframes import NEAAbschnittDataframes
from .nea_abschnitt_dictionary import NEAAbschnittDictionary


class NEAAbschnittDataframesFactory:
    def create(self, abschnitt: NEAAbschnitt, sektoren: list[NEASektor], bereiche: list[NEABereich],
               abschnitt_dictionary: NEAAbschnittDictionary) -> NEAAbschnittDataframes:
        pass
