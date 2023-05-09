from Domain.Energiebilanz import EBEnergietraegerFactory, EBSektorenFactory, EBDataFactory
from Domain.General import GData
from Processor.eb_processor import EBProcessor


class EBProcessorFactory:
    def __init__(self, eb_data_factory: EBDataFactory):
        self.__eb_data_factory = eb_data_factory

    def create(self, g_data: GData):
        eb_data = self.__eb_data_factory.create(g_data)
        return EBProcessor(eb_data)
