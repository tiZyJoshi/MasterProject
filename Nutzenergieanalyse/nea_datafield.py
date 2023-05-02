from dataclasses import dataclass

import pandas as pd

from Nutzenergieanalyse.nea_energietraeger import NEAEnergietraeger
from Nutzenergieanalyse.nea_jahr import NEAJahr
from Nutzenergieanalyse.nea_sektor import NEASektor


@dataclass
class NEADataField:
    jahr: NEAJahr
    sektor: NEASektor
    energietraeger: NEAEnergietraeger
    data: pd.Series

    def __hash__(self):
        return hash((self.jahr, self.sektor, self.energietraeger))
