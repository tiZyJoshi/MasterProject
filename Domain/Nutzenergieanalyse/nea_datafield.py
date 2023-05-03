from dataclasses import dataclass

import pandas as pd

from .nea_energietraeger import NEAEnergietraeger
from .nea_jahr import NEAJahr
from .nea_sektor import NEASektor


@dataclass
class NEADataField:
    jahr: NEAJahr
    sektor: NEASektor
    energietraeger: NEAEnergietraeger
    data: pd.Series

    def __hash__(self):
        return hash((self.jahr, self.sektor, self.energietraeger))

