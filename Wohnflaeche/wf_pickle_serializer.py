import pathlib

from Domain.Wohnflaeche import WFDataSerializer, WFData
from .wf_pickle_path_factory import WFPicklePathFactory


class WFPickleSerializer(WFDataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = WFPicklePathFactory(path)

    def run(self, data: WFData):
        for land in data.laender:
            ser_path = self.__path_factory.create(land)
            ser_path.parent.mkdir(parents=True, exist_ok=True)
            data.data[land].to_pickle(ser_path)
