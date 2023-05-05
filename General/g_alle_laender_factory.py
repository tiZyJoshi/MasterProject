from Domain.General import GLaenderFactory, GLand
from .g_oesterreich_factory import GOesterreichFactory
from .g_bundeslaender_factory import GBundeslaenderFactory


class GAlleLaenderFactory(GLaenderFactory):
    def __init__(self):
        self.__oesterreich_factory = GOesterreichFactory()
        self.__bundeslaender_factory = GBundeslaenderFactory()

    def create(self) -> dict[str, GLand]:
        oesterreich = self.__oesterreich_factory.create()
        bundeslaender = self.__bundeslaender_factory.create()
        return oesterreich | bundeslaender
