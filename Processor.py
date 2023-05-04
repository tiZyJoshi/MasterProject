import pathlib

from Domain.Energiebilanz import EBData, EBEnergietraegerFactory, EBSektorenFactory, EBDataFactory
from Domain.Nutzenergieanalyse import NEAData, NEADataFactory, NEAAbschnitteFactory, NEASektorenFactory, \
    NEABereicheFactory
from Domain.Bevoelkerung import BData, BDataFactory
from Domain.General import GLand

from Energiebilanz import EBDataValidator, EBPickleSerializer, EBExcelSerializer
from Nutzenergieanalyse import NEADataValidator, NEAPickleSerializer, NEAExcelSerializer
from Bevoelkerung import BPickleSerializer


class NEAProcessorFactory:
    def __init__(self, nea_abschnitte_factory: NEAAbschnitteFactory,
                 nea_sektoren_factory: NEASektorenFactory, nea_bereiche_factory: NEABereicheFactory,
                 nea_data_factory: NEADataFactory):
        self.__nea_abschnitte_factory = nea_abschnitte_factory
        self.__nea_sektoren_factory = nea_sektoren_factory
        self.__nea_bereiche_factory = nea_bereiche_factory
        self.__nea_data_factory = nea_data_factory

    def create(self):
        nea_abschnitte = self.__nea_abschnitte_factory.create()
        nea_sektoren = self.__nea_sektoren_factory.create()
        nea_bereiche = self.__nea_bereiche_factory.create()
        nea_data = self.__nea_data_factory.create(nea_abschnitte, nea_sektoren, nea_bereiche)
        return NEAProcessor(nea_data)


class NEAProcessor:
    def __init__(self, nea_data: NEAData):
        self.__nea_data = nea_data

    def run_validation(self):
        validator = NEADataValidator()
        total_sum = validator.create_total_sum(self.__nea_data)
        print(total_sum)

    def run_pickle_serialization(self):
        serializer = NEAPickleSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__nea_data)

    def run_excel_serialization(self):
        serializer = NEAExcelSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__nea_data)


class EBProcessorFactory:
    def __init__(self, eb_energietraeger_factory: EBEnergietraegerFactory, eb_sektoren_factory: EBSektorenFactory,
                 eb_data_factory: EBDataFactory):
        self.__eb_energietraeger_factory = eb_energietraeger_factory
        self.__eb_sektoren_factory = eb_sektoren_factory
        self.__eb_data_factory = eb_data_factory

    def create(self):
        eb_energietraeger = self.__eb_energietraeger_factory.create()
        eb_sektoren = self.__eb_sektoren_factory.create()
        eb_data = self.__eb_data_factory.create(eb_energietraeger, eb_sektoren)
        return EBProcessor(eb_data)


class EBProcessor:
    def __init__(self, eb_data: EBData):
        self.__eb_data = eb_data

    def run_validation(self):
        validator = EBDataValidator()
        total_sum = validator.create_total_sum(self.__eb_data)
        print(total_sum)

    def run_pickle_serialization(self):
        serializer = EBPickleSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__eb_data)

    def run_excel_serialization(self):
        serializer = EBExcelSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__eb_data)


class BProcessorFactory:
    def __init__(self, b_data_factory: BDataFactory, laender: list[GLand]):
        self.__b_data_factory = b_data_factory
        self.__laender = laender

    def create(self):
        b_data = self.__b_data_factory.create(self.__laender)
        return BProcessor(b_data)


class BProcessor:
    def __init__(self, b_data: BData):
        self.__b_data = b_data

    def run_pickle_serialization(self):
        serializer = BPickleSerializer(pathlib.Path('Data/Serialization'))
        serializer.run(self.__b_data)
