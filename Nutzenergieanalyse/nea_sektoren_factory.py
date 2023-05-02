from General.GSektor import GSektor
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEASektorenFactory:
    def __init__(self, sektoren: dict[str, GSektor]):
        self.__sektoren = sektoren

    def create_nea_sektoren(self):
        return [NEASektor('Wohngebäude', 602, self.__sektoren['Wohngebäude']),
                NEASektor('Dienstleistungsgebäude', 576, self.__sektoren['Dienstleistungsgebäude']),
                NEASektor('Landwirtschaftsgebäude', 628, self.__sektoren['Landwirtschaftsgebäude'])]
