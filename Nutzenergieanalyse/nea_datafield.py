from dataclasses import dataclass

import pandas as pd

from Domain.Nutzenergieanalyse import NEAJahr, NEASektor, NEAEnergietraeger


@dataclass
class NEADataField:
    jahr: NEAJahr
    sektor: NEASektor
    energietraeger: NEAEnergietraeger
    data: pd.Series

    def __hash__(self):
        return hash((self.jahr, self.sektor, self.energietraeger))

