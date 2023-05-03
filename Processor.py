from Domain.General import GEnergietraeger, GLand, GSektor, GEnergietraegerFactory, GLaenderFactory, GSektorenFactory
from Domain.Nutzenergieanalyse import NEAData


class GeneralData:
    def __init__(self, laender: dict[str, GLand], sektoren: dict[str, GSektor],
                 energietraeger: dict[str, GEnergietraeger]):
        self.laender = laender
        self.sektoren = sektoren
        self.energietraeger = energietraeger


class GeneralDataFactory:
    def __init__(self, laender_factory: GLaenderFactory, sektoren_factory: GSektorenFactory,
                 energietraeger_factory: GEnergietraegerFactory):
        self.__laender_factory = laender_factory
        self.__sektoren_factory = sektoren_factory
        self.__energietraeger_factory = energietraeger_factory

    def create(self):
        laender = self.__laender_factory.create()
        sektoren = self.__sektoren_factory.create()
        energietraeger = self.__energietraeger_factory.create()
        return GeneralData(laender, sektoren, energietraeger)


class ProcessorFactory:
    def __init__(self, general_data_factory: GeneralDataFactory):
        self.__general_data_factory = general_data_factory

    def create(self):
        pass


class Processor:
    def __init__(self, general_data: GeneralData, nea_data: NEAData):
        self.__nea_data = nea_data
