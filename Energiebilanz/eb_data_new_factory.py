from Domain.Energiebilanz import EBFilesFactory, EBFile, EBEnergietraeger, EBSektor
from Domain.Energiebilanz.eb_data import EBData
from Domain.Energiebilanz.eb_data_factory import EBDataFactory
from Energiebilanz.eb_file_data_factory import EBFileDataFactory
from Energiebilanz.eb_file_dataframes_factory import EBFileDataframesFactory
from Energiebilanz.eb_file_dictionary_factory import EBFileDictionaryFactory


class EBDataNewFactory(EBDataFactory):
    __ABC = str

    def __init__(self,
                 files_factory: EBFilesFactory,
                 data_factory: EBFileDataFactory,
                 dictionary_factory: EBFileDictionaryFactory,
                 dataframes_factory: EBFileDataframesFactory):
        self.__files_factory = files_factory
        self.__data_factory = data_factory
        self.__dictionary_factory = dictionary_factory
        self.__dataframes_factory = dataframes_factory

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
