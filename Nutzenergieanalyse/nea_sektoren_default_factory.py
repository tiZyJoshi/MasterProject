from Domain.General import GSektor
from Domain.Nutzenergieanalyse import NEASektor, NEASektorenFactory, NEABereich


class NEASektorenVor2005Factory(NEASektorenFactory):
    def __init__(self, sektoren: dict[str, GSektor], default_bereiche: list[NEABereich]):
        self.__sektoren = sektoren
        self.__default_bereiche = default_bereiche

    def create(self) -> list[NEASektor]:
        return [NEASektor('Wohngebäude', 602, 'A:H', self.__default_bereiche, self.__sektoren['Wohngebäude']),
                NEASektor('Dienstleistungsgebäude', 576, 'A:H', self.__default_bereiche,
                          self.__sektoren['Dienstleistungsgebäude']),
                NEASektor('Landwirtschaftsgebäude', 628, 'A:H', self.__default_bereiche,
                          self.__sektoren['Landwirtschaftsgebäude'])]


class NEASektorenAb2005Factory(NEASektorenFactory):
    def __init__(self, sektoren: dict[str, GSektor], default_bereiche: list[NEABereich],
                 haushalte_ab_2005_bereiche: list[NEABereich]):
        self.__sektoren = sektoren
        self.__default_bereiche = default_bereiche
        self.__haushalte_ab_2005_bereiche = haushalte_ab_2005_bereiche

    def create(self) -> list[NEASektor]:
        return [
            NEASektor('Wohngebäude', 602, 'U:AE', self.__haushalte_ab_2005_bereiche, self.__sektoren['Wohngebäude']),
            NEASektor('Dienstleistungsgebäude', 576, 'A:H', self.__default_bereiche,
                      self.__sektoren['Dienstleistungsgebäude']),
            NEASektor('Landwirtschaftsgebäude', 628, 'A:H', self.__default_bereiche,
                      self.__sektoren['Landwirtschaftsgebäude'])]
