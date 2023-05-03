import pandas as pd

from Domain.Nutzenergieanalyse import NEABereich, NEASektor

NEAAbschnittDataframes = dict[NEASektor, dict[NEABereich, pd.DataFrame]]
