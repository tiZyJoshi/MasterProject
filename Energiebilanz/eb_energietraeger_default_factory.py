from Domain.Energiebilanz import EBEnergietraeger, EBEnergietraegerFactory
from Domain.General import GEnergietraeger


class EBEnergietraegerDefaultFactory(EBEnergietraegerFactory):
    def __init__(self, energietraeger: dict[str, GEnergietraeger]):
        self.__energietraeger = energietraeger

    def create(self) -> list[EBEnergietraeger]:
        return [EBEnergietraeger('Braunkohle', self.__energietraeger['Braunkohle']),
                EBEnergietraeger('Braunkohlen-Briketts', self.__energietraeger['Braunkohlen-Briketts']),
                EBEnergietraeger('Brenntorf', self.__energietraeger['Brenntorf']),
                EBEnergietraeger('Koks', self.__energietraeger['Koks']),
                EBEnergietraeger('Steinkohle', self.__energietraeger['Steinkohle']),
                EBEnergietraeger('Benzin', self.__energietraeger['Benzin']),
                EBEnergietraeger('Diesel', self.__energietraeger['Diesel']),
                EBEnergietraeger('Gasöl für Heizzwecke', self.__energietraeger['Heiz-Gasöl']),
                EBEnergietraeger('Petroleum', self.__energietraeger['Petroleum']),
                EBEnergietraeger('Heizöl', self.__energietraeger['Heizöl']),
                EBEnergietraeger('Flüssiggas', self.__energietraeger['Flüssiggas']),
                EBEnergietraeger('Erdgas', self.__energietraeger['Erdgas']),
                EBEnergietraeger('Mischgas', self.__energietraeger['Mischgas']),
                EBEnergietraeger('Brennbare Abfälle', self.__energietraeger['Brennbare Abfälle']),
                EBEnergietraeger('Scheitholz', self.__energietraeger['Scheitholz']),
                EBEnergietraeger('Biogene Brenn- u. Treibstoffe', self.__energietraeger['Biogene']),
                EBEnergietraeger('Umgebungswärme etc.', self.__energietraeger['Erneuerbare']),
                EBEnergietraeger('Fernwärme', self.__energietraeger['Fernwärme']),
                EBEnergietraeger('Elektrische Energie', self.__energietraeger['Elektrische Energie'])]
