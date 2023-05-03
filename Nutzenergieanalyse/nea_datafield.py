from dataclasses import dataclass

import pandas as pd

from Domain.Nutzenergieanalyse import NEAEnergietraeger, NEAJahr, NEASektor


@dataclass
class NEADataField:
    jahr: NEAJahr
    sektor: NEASektor
    energietraeger: NEAEnergietraeger
    data: pd.Series

    def __hash__(self):
        return hash((self.jahr, self.sektor, self.energietraeger))

