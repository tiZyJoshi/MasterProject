from Domain.Bevoelkerung import BDataFactory
from Domain.General import GLand
from Processor.b_processor import BProcessor


class BProcessorFactory:
    def __init__(self, b_data_factory: BDataFactory, laender: list[GLand]):
        self.__b_data_factory = b_data_factory
        self.__laender = laender

    def create(self):
        b_data = self.__b_data_factory.create(self.__laender)
        return BProcessor(b_data)
