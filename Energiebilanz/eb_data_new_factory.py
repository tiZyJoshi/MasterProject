from Domain.Energiebilanz import EBFilesFactory, EBFile, EBEnergietraeger, EBSektor, EBData, EBDataFactory
from .eb_file_data_factory import EBFileDataFactory
from .eb_file_dataframes_factory import EBFileDataframesFactory
from .eb_file_dictionary_factory import EBFileDictionaryFactory


class EBDataNewFactory(EBDataFactory):
    def __init__(self, files_factory: EBFilesFactory):
        self.__files_factory = files_factory
        self.__data_factory = EBFileDataFactory()
        self.__dictionary_factory = EBFileDictionaryFactory()
        self.__dataframes_factory = EBFileDataframesFactory()

    def __load(self, file: EBFile, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]):
        file_data_fields = self.__data_factory.create(file, energietraeger, sektoren)
        file_dictionary = self.__dictionary_factory.create(sektoren, file_data_fields)
        file_dataframes = self.__dataframes_factory.create(sektoren, file_dictionary)
        return file_dataframes

    def create(self, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]) -> EBData:
        files = self.__files_factory.create()
        laender = list([file.land for file in files])
        return EBData(laender, energietraeger, sektoren, {
            file.land: self.__load(file, energietraeger, sektoren) for file in files})
