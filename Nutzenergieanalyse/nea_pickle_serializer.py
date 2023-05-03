import pathlib

from Domain.Nutzenergieanalyse import NEAData, NEADataSerializer
from .nea_pickle_path_factory import NEAPicklePathFactory


class NEAPickleSerializer(NEADataSerializer):
    def __init__(self, path: pathlib.Path):
        self.__path_factory = NEAPicklePathFactory(path)

    def run(self, data: NEAData):
        for land in data.laender:
            for abschnitt in data.abschnitte:
                for sektor in data.sektoren:
                    for bereich in data.bereiche:
                        ser_path = self.__path_factory.create(land, abschnitt, sektor, bereich)
                        ser_path.parent.mkdir(parents=True, exist_ok=True)
                        data.data[land][abschnitt][sektor][bereich].to_pickle(ser_path)
