from dataclasses import dataclass

import pandas as pd

from .eb_land import EBLand
from .eb_energietraeger import EBEnergietraeger
from .eb_sektor import EBSektor


@dataclass
class EBData:
    laender: list[EBLand]
    energietraeger: list[EBEnergietraeger]
    sektoren: list[EBSektor]
    data: dict[EBLand, dict[EBSektor, pd.DataFrame]]
