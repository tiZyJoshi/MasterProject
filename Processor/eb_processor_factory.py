from Domain.Energiebilanz import EBEnergietraegerFactory, EBSektorenFactory, EBDataFactory
from Domain.General import GData
from Processor.eb_processor import EBProcessor


class EBProcessorFactory:
    def __init__(self, eb_energietraeger_factory: EBEnergietraegerFactory, eb_sektoren_factory: EBSektorenFactory,
                 eb_data_factory: EBDataFactory):
        self.__eb_energietraeger_factory = eb_energietraeger_factory
        self.__eb_sektoren_factory = eb_sektoren_factory
        self.__eb_data_factory = eb_data_factory

    def create(self, g_data: GData):
        eb_energietraeger = self.__eb_energietraeger_factory.create(g_data)
        eb_sektoren = self.__eb_sektoren_factory.create()
        eb_data = self.__eb_data_factory.create(eb_energietraeger, eb_sektoren)
        return EBProcessor(eb_data)
