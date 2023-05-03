from Domain.Nutzenergieanalyse import NEAData, NEADataFactory, NEAAbschnitteFactory, NEASektorenFactory, \
    NEABereicheFactory
from Domain.General import GData, GDataFactory

from Nutzenergieanalyse import NEADataValidator


class ProcessorFactory:
    def __init__(self, general_data_factory: GDataFactory, nea_abschnitte_factory: NEAAbschnitteFactory,
                 nea_sektoren_factory: NEASektorenFactory, nea_bereiche_factory: NEABereicheFactory,
                 nea_data_factory: NEADataFactory):
        self.__general_data_factory = general_data_factory
        self.__nea_abschnitte_factory = nea_abschnitte_factory
        self.__nea_sektoren_factory = nea_sektoren_factory
        self.__nea_bereiche_factory = nea_bereiche_factory
        self.__nea_data_factory = nea_data_factory

    def create(self):
        general_data = self.__general_data_factory.create()
        nea_abschnitte = self.__nea_abschnitte_factory.create()
        nea_sektoren = self.__nea_sektoren_factory.create()
        nea_bereiche = self.__nea_bereiche_factory.create()
        nea_data = self.__nea_data_factory.create(nea_abschnitte, nea_sektoren, nea_bereiche)
        return Processor(general_data, nea_data)


class Processor:
    def __init__(self, general_data: GData, nea_data: NEAData):
        self.__nea_data = nea_data

    def run(self):
        validator = NEADataValidator(self.__nea_data)
        total_sum = validator.create_total_sum()
        print(total_sum)
