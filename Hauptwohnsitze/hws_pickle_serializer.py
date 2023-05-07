import pathlib

from Domain.Hauptwohnsitze import HWSDataSerializer, HWSData
from .hws_pickle_path_factory import HWSPicklePathFactory


class HWSPickleSerializer(HWSDataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = HWSPicklePathFactory(path)

    def run(self, data: HWSData):
        for land in data.laender:
            ser_path = self.__path_factory.create(land)
            ser_path.parent.mkdir(parents=True, exist_ok=True)
            data.data[land].to_pickle(ser_path)
