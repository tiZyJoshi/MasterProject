from Domain.General import GLaenderFactory, GSektorenFactory, GBereicheFactory, GEnergietraegerFactory, \
    GEnergietraegerKlassenFactory, GData


class GDataFactory:
    def __init__(self, laender_factory: GLaenderFactory, sektoren_factory: GSektorenFactory,
                 bereiche_factory: GBereicheFactory, energietraeger_klassen_factory: GEnergietraegerKlassenFactory,
                 energietraeger_factory: GEnergietraegerFactory):
        self.__laender_factory = laender_factory
        self.__sektoren_factory = sektoren_factory
        self.__bereiche_factory = bereiche_factory
        self.__energietraeger_klassen_factory = energietraeger_klassen_factory
        self.__energietraeger_factory = energietraeger_factory

    def create(self):
        laender = self.__laender_factory.create()
        sektoren = self.__sektoren_factory.create()
        bereiche = self.__bereiche_factory.create()
        energietraeger_klassen = self.__energietraeger_klassen_factory.create()
        energietraeger = self.__energietraeger_factory.create(energietraeger_klassen)
        return GData(laender, sektoren, bereiche, energietraeger_klassen, energietraeger)
