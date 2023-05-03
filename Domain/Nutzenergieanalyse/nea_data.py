from dataclasses import dataclass
import pandas as pd

from .nea_abschnitt import NEAAbschnitt
from .nea_bereich import NEABereich
from .nea_land import NEALand
from .nea_sektor import NEASektor


@dataclass
class NEAData:
    laender: list[NEALand]
    abschnitte: list[NEAAbschnitt]
    sektoren: list[NEASektor]
    bereiche: list[NEABereich]
    data: dict[NEALand, dict[NEAAbschnitt, dict[NEASektor, dict[NEABereich, pd.DataFrame]]]]
