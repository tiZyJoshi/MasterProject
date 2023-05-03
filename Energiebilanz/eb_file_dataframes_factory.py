import pandas as pd

from Domain.Energiebilanz import EBSektor
from Energiebilanz.eb_file_dataframes import EBFileDataframes
from Energiebilanz.eb_file_dictionary import EBFileDictionary


class EBFileDataframesFactory:
    @staticmethod
    def create(sektoren: list[EBSektor], file_dictionary: EBFileDictionary) -> EBFileDataframes:
        return {sektor: pd.concat(file_dictionary[sektor].values(), axis=1) for sektor in sektoren}
