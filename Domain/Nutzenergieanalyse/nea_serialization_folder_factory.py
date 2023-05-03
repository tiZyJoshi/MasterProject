from .nea_abschnitt import NEAAbschnitt
from .nea_land import NEALand
from .nea_sektor import NEASektor


class NEASerializationFolderFactory:
    def create(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor):
        pass
