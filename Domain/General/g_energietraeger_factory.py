from .g_energietraeger import GEnergietraeger
from .g_energietraeger_klasse import GEnergietraegerKlasse


class GEnergietraegerFactory:
    def create(self, klassen: dict[str, GEnergietraegerKlasse]) -> dict[str, GEnergietraeger]:
        pass
