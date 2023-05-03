from Domain.Energiebilanz import EBSektor, EBSektorenFactory
from Domain.General import GSektor


class EBSektorenDefaultFactory(EBSektorenFactory):
    def __init__(self, sektoren: dict[str, GSektor]):
        self.__sektoren = sektoren

    def create(self) -> list[EBSektor]:
        return [EBSektor('Private Haushalte', self.__sektoren['Wohngebäude']),
                EBSektor('Öffentliche und Private Dienstleistungen', self.__sektoren['Dienstleistungsgebäude']),
                EBSektor('Landwirtschaft', self.__sektoren['Landwirtschaftsgebäude'])]
