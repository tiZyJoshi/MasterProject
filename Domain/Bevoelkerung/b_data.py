from dataclasses import dataclass

import pandas as pd

from Domain.General import GLand


@dataclass
class BData:
    laender: list[GLand]
    data: dict[GLand, pd.Series]
