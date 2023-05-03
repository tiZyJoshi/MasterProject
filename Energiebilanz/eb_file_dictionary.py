import pandas as pd

from Domain.Energiebilanz import EBSektor, EBEnergietraeger

EBFileDictionary = dict[EBSektor, dict[EBEnergietraeger, pd.Series]]
