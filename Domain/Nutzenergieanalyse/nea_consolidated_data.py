from dataclasses import dataclass
import pandas as pd

from .nea_bereich_klasse import NEABereichKlasse
from Domain.General import GLand, GSektor


@dataclass
class NEAConsolidatedData:
    laender: list[GLand]
    sektoren: list[GSektor]
    bereiche: list[NEABereichKlasse]
    data: dict[GLand, dict[GSektor, dict[NEABereichKlasse, pd.DataFrame]]]
