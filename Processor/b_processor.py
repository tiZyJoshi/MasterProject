import pathlib

from Bevoelkerung import BPickleSerializer
from Domain.Bevoelkerung import BData


class BProcessor:
    def __init__(self, b_data: BData):
        self.__b_data = b_data

    def run_pickle_serialization(self):
        serializer = BPickleSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__b_data)
