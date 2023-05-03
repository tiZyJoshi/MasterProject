from dataclasses import dataclass

import pandas as pd

from Domain.Energiebilanz import EBEnergietraeger, EBSektor


@dataclass
class EBDataField:
    sektor: EBSektor
    energietraeger: EBEnergietraeger
    data: pd.Series

    def __hash__(self):
        return hash((self.sektor, self.energietraeger))
