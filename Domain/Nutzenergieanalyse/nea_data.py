from dataclasses import dataclass

import pandas as pd

from Domain.General import GLand, GSektor, GBereich


@dataclass
class NEAData:
    data: dict[GLand, dict[GSektor, dict[GBereich, pd.DataFrame]]]
