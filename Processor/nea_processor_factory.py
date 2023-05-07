from Domain.General import GData
from Domain.Nutzenergieanalyse import NEADataFactory
from Processor.nea_processor import NEAProcessor


class NEAProcessorFactory:
    def __init__(self, nea_data_factory: NEADataFactory):
        self.__nea_data_factory = nea_data_factory

    def create(self, g_data: GData):
        nea_data = self.__nea_data_factory.create(g_data)
        return NEAProcessor(nea_data)
