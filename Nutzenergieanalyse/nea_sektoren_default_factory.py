from Domain.General import GSektor
from Domain.Nutzenergieanalyse import NEASektor, NEASektorenFactory


class NEASektorenDefaultFactory(NEASektorenFactory):
    def __init__(self, sektoren: dict[str, GSektor]):
        self.__sektoren = sektoren

    def create(self) -> list[NEASektor]:
        return [NEASektor('Wohngebäude', 602, self.__sektoren['Wohngebäude']),
                NEASektor('Dienstleistungsgebäude', 576, self.__sektoren['Dienstleistungsgebäude']),
                NEASektor('Landwirtschaftsgebäude', 628, self.__sektoren['Landwirtschaftsgebäude'])]
