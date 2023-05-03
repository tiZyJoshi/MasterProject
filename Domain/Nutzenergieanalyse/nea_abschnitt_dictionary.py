import pandas as pd

from .nea_jahr import NEAJahr
from .nea_sektor import NEASektor

from .nea_energietraeger import NEAEnergietraeger

NEAAbschnittDictionary = dict[NEAJahr, dict[NEASektor, dict[NEAEnergietraeger, pd.Series]]]
