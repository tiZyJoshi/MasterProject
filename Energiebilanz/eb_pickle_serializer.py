from Domain.Energiebilanz.eb_data import EBData
from Domain.Energiebilanz.eb_data_serializer import EBDataSerializer
from Domain.Energiebilanz.eb_serialization_folder_factory import EBSerializationFolderFactory


class EBPickleSerializer(EBDataSerializer):
    def __init__(self, folder_factory: EBSerializationFolderFactory):
        self.__folder_factory = folder_factory

    def run(self, data: EBData):
        for land in data.laender:
            for sektor in data.sektoren:
                ser_path = self.__folder_factory.create(land, sektor)
                ser_path.mkdir(parents=True, exist_ok=True)
                data.data[land][sektor].to_pickle(ser_path / f'{sektor.name}.pkl')
