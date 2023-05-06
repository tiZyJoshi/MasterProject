from dataclasses import dataclass

import pandas as pd

from Domain.General import GLand, GSektor


@dataclass
class EBData:
    data: dict[GLand, dict[GSektor, pd.DataFrame]]
