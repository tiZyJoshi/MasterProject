from dataclasses import dataclass

from .g_bereich import GBereich
from .g_land import GLand
from .g_sektor import GSektor
from .g_energietraeger import GEnergietraeger


@dataclass
class GData:
    laender: dict[str, GLand]
    sektoren: dict[str, GSektor]
    bereiche: dict[str, GBereich]
    energietraeger: dict[str, GEnergietraeger]
