import pathlib

from Domain.Nutzenergieanalyse import NEAData, NEADataSerializer
from .nea_pickle_path_factory import NEAPicklePathFactory


class NEAPickleSerializer(NEADataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = NEAPicklePathFactory(path)

    def run(self, data: NEAData):
        for land in data.data.keys():
            for sektor in data.data[land].keys():
                for bereich in data.data[land][sektor].keys():
                    ser_path = self.__path_factory.create(land, sektor, bereich)
                    ser_path.parent.mkdir(parents=True, exist_ok=True)
                    data.data[land][sektor][bereich].to_pickle(ser_path)
