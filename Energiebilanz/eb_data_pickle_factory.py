import pandas as pd

from Domain.Energiebilanz import EBLand, EBSektor, EBEnergietraeger
from Domain.Energiebilanz.eb_data import EBData
from Domain.Energiebilanz.eb_serialization_folder_factory import EBSerializationFolderFactory


class EBDataPickleFactory(EBData):
    def __init__(self, folder_factory: EBSerializationFolderFactory, laender: list[EBLand]):
        self.__laender = laender
        self.__folder_factory = folder_factory

    def __read_eb_pickle(self, land: EBLand, sektor: EBSektor):
        ser_path = self.__folder_factory.create(land, sektor)
        return pd.read_pickle(ser_path / f'{sektor.name}.pkl')

    def __restore_eb_dataframes(self, land: EBLand, sektoren: list[EBSektor]):
        return {sektor: self.__read_eb_pickle(land, sektor) for sektor in sektoren}

    def create(self, sektoren: list[EBSektor], energietraeger: list[EBEnergietraeger]) -> EBData:
        return EBData(self.__laender, energietraeger, sektoren, {
            land: self.__restore_eb_dataframes(land, sektoren) for land in self.__laender})
