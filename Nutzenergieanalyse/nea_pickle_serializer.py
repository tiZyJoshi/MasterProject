from Domain.Nutzenergieanalyse import NEAData, NEADataSerializer, NEASerializationFolderFactory


class NEAPickleSerializer(NEADataSerializer):
    def __init__(self, folder_factory: NEASerializationFolderFactory):
        self.__folder_factory = folder_factory

    def run(self, data: NEAData):
        for land in data.laender:
            for abschnitt in data.abschnitte:
                for sektor in data.sektoren:
                    for bereich in data.bereiche:
                        ser_path = self.__folder_factory.create(land, abschnitt, sektor)
                        ser_path.mkdir(parents=True, exist_ok=True)
                        data.data[land][abschnitt][sektor][bereich].to_pickle(ser_path / f'{bereich.name}.pkl')
