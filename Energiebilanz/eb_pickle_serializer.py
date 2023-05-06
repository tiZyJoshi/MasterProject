import pathlib

from Domain.Energiebilanz import EBData, EBDataSerializer

from .eb_pickle_path_factory import EBPicklePathFactory


class EBPickleSerializer(EBDataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = EBPicklePathFactory(path)

    def run(self, data: EBData):
        for land in data.data.keys():
            for sektor in data.data[land].keys():
                ser_path = self.__path_factory.create(land, sektor)
                ser_path.parent.mkdir(parents=True, exist_ok=True)
                data.data[land][sektor].to_pickle(ser_path)
