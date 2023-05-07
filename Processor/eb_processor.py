import pathlib

from Domain.Energiebilanz import EBData
from Energiebilanz import EBDataValidator, EBPickleSerializer, EBExcelSerializer


class EBProcessor:
    def __init__(self, eb_data: EBData):
        self.__eb_data = eb_data

    def run_validation(self):
        validator = EBDataValidator()
        total_sum = validator.create_total_sum(self.__eb_data)
        print(total_sum)

    def run_pickle_serialization(self):
        serializer = EBPickleSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__eb_data)

    def run_excel_serialization(self):
        serializer = EBExcelSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__eb_data)
