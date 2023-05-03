from dataclasses import dataclass

import pandas as pd

from .eb_energietraeger import EBEnergietraeger
from .eb_sektor import EBSektor


@dataclass
class EBDataField:
    sektor: EBSektor
    energietraeger: EBEnergietraeger
    data: pd.Series

    def __hash__(self):
        return hash((self.sektor, self.energietraeger))
