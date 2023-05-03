from Domain.General import GEnergietraeger, GEnergietraegerKlasse, GEnergietraegerFactory


class GEnergietraegerDefaultFactory(GEnergietraegerFactory):
    def __init__(self, klassen: dict[str, GEnergietraegerKlasse]):
        self.__klassen = klassen

    def create(self) -> dict[str, GEnergietraeger]:
        energietraeger_list = [GEnergietraeger('Braunkohle', self.__klassen['Fossile fest']),
                               GEnergietraeger('Braunkohlen-Briketts', self.__klassen['Fossile fest']),
                               GEnergietraeger('Brenntorf', self.__klassen['Fossile fest']),
                               GEnergietraeger('Koks', self.__klassen['Fossile fest']),
                               GEnergietraeger('Steinkohle', self.__klassen['Fossile fest']),
                               GEnergietraeger('Benzin', self.__klassen['Fossile flüssig']),
                               GEnergietraeger('Diesel', self.__klassen['Fossile flüssig']),
                               GEnergietraeger('Heiz-Gasöl', self.__klassen['Fossile flüssig']),
                               GEnergietraeger('Petroleum', self.__klassen['Fossile flüssig']),
                               GEnergietraeger('Heizöl', self.__klassen['Fossile flüssig']),
                               GEnergietraeger('Flüssiggas', self.__klassen['Fossile flüssig']),
                               GEnergietraeger('Erdgas', self.__klassen['Fossile gasförmig']),
                               GEnergietraeger('Mischgas', self.__klassen['Fossile gasförmig']),
                               GEnergietraeger('Brennbare Abfälle', self.__klassen['Brennbare Abfälle']),
                               GEnergietraeger('Scheitholz', self.__klassen['Scheitholz']),
                               GEnergietraeger('Biogene', self.__klassen['Biogene']),
                               GEnergietraeger('Erneuerbare', self.__klassen['Erneuerbare']),
                               GEnergietraeger('Fernwärme', self.__klassen['Fernwärme']),
                               GEnergietraeger('Elektrische Energie', self.__klassen['Elektrische Energie'])]
        return {energietraeger.name: energietraeger for energietraeger in energietraeger_list}
