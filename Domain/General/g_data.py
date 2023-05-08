from dataclasses import dataclass

from .g_bereich import GBereich
from .g_land import GLand
from .g_sektor import GSektor
from .g_energietraeger import GEnergietraeger
from .g_energietraeger import GEnergietraegerKlasse


@dataclass
class GData:
    laender: dict[str, GLand]
    sektoren: dict[str, GSektor]
    bereiche: dict[str, GBereich]
    energietraeger_klassen: dict[str, GEnergietraegerKlasse]
    energietraeger: dict[str, GEnergietraeger]
