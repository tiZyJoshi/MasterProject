import pathlib

from Domain.Nutzenergieanalyse import NEAData
from Nutzenergieanalyse import NEADataValidator, NEAPickleSerializer, NEAExcelSerializer


class NEAProcessor:
    def __init__(self, nea_data: NEAData):
        self.__nea_data = nea_data

    def run_validation(self):
        validator = NEADataValidator()
        total_sum = validator.create_total_sum(self.__nea_data)
        print(total_sum)

    def run_pickle_serialization(self):
        serializer = NEAPickleSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__nea_data)

    def run_excel_serialization(self):
        serializer = NEAExcelSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__nea_data)
