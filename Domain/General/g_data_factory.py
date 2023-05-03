from .g_laender_factory import GLaenderFactory
from .g_sektoren_factory import GSektorenFactory
from .g_energietraeger_factory import GEnergietraegerFactory
from .g_data import GData


class GDataFactory:
    def __init__(self, laender_factory: GLaenderFactory, sektoren_factory: GSektorenFactory,
                 energietraeger_factory: GEnergietraegerFactory):
        self.__laender_factory = laender_factory
        self.__sektoren_factory = sektoren_factory
        self.__energietraeger_factory = energietraeger_factory

    def create(self):
        laender = self.__laender_factory.create()
        sektoren = self.__sektoren_factory.create()
        energietraeger = self.__energietraeger_factory.create()
        return GData(laender, sektoren, energietraeger)
