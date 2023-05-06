import pandas as pd

from Domain.General import GBereich, GSektor

NEAAbschnittDataframes = dict[GSektor, dict[GBereich, pd.DataFrame]]
