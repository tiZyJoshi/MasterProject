import pandas as pd

from Domain.Nutzenergieanalyse import NEAJahr, NEASektor, NEAEnergietraeger


NEAAbschnittDictionary = dict[NEAJahr, dict[NEASektor, dict[NEAEnergietraeger, pd.Series]]]
