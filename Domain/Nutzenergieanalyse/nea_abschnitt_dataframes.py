import pandas as pd

from .nea_bereich import NEABereich
from .nea_sektor import NEASektor

NEAAbschnittDataframes = dict[NEASektor, dict[NEABereich, pd.DataFrame]]
