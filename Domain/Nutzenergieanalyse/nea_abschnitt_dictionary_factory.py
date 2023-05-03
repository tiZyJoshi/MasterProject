from .nea_abschnitt_dictionary import NEAAbschnittDictionary
from .nea_bereich import NEABereich
from .nea_jahr import NEAJahr
from .nea_sektor import NEASektor
from .nea_datafield import NEADataField


class NEAAbschnittDictionaryFactory:
    def create(self, jahre: list[NEAJahr], sektoren: list[NEASektor], bereiche: list[NEABereich],
               data_fields: list[NEADataField]) -> NEAAbschnittDictionary:
        pass
