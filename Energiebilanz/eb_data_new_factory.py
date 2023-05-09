from Domain.Energiebilanz import EBFilesFactory, EBFile, EBEnergietraeger, EBSektor, EBData, EBDataFactory
from Domain.General import GData
from .eb_file_data_factory import EBFileDataFactory
from .eb_file_dataframes_factory import EBFileDataframesFactory
from .eb_file_dictionary_factory import EBFileDictionaryFactory
from .eb_energietraeger_default_factory import EBEnergietraegerDefaultFactory
from .eb_sektoren_default_factory import EBSektorenDefaultFactory


class EBDataNewFactory(EBDataFactory):
    def __init__(self, files_factory: EBFilesFactory):
        self.__files_factory = files_factory
        self.__energietraeger_factory = EBEnergietraegerDefaultFactory()
        self.__sektoren_factory = EBSektorenDefaultFactory()
        self.__data_factory = EBFileDataFactory()
        self.__dictionary_factory = EBFileDictionaryFactory()
        self.__dataframes_factory = EBFileDataframesFactory()

    def __load(self, file: EBFile, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]):
        file_data_fields = self.__data_factory.create(file, energietraeger, sektoren)
        file_dictionary = self.__dictionary_factory.create(sektoren, file_data_fields)
        file_dataframes = self.__dataframes_factory.create(sektoren, file_dictionary)
        return file_dataframes

    def create(self, g_data: GData) -> EBData:
        files = self.__files_factory.create()
        energietraeger = self.__energietraeger_factory.create(g_data)
        sektoren = self.__sektoren_factory.create(g_data)
        return EBData({file.land.entspricht: self.__load(file, energietraeger, sektoren) for file in files})
