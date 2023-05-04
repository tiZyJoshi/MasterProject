import pathlib

from .b_pickle_path_factory import BPicklePathFactory
from Domain.Bevoelkerung import BDataSerializer, BData


class BPickleSerializer(BDataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = BPicklePathFactory(path)

    def run(self, data: BData):
        for land in data.laender:
            ser_path = self.__path_factory.create(land)
            ser_path.parent.mkdir(parents=True, exist_ok=True)
            data.data[land].to_pickle(ser_path)
