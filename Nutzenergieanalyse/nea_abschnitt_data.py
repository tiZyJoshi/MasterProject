from Nutzenergieanalyse.nea_abschnitt_dictionary import NEAAbschnittDictionary
from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_datafield import NEADataField
from Nutzenergieanalyse.nea_jahr import NEAJahr
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEAAbschnittData:
    def __init__(self, land: NEALand, sektoren: list[NEASektor], bereiche: list[NEABereich], data: list[NEADataField]):
        self.land = land
        self.__sektoren = sektoren
        self.__bereiche = bereiche
        self.__data = data

    def __create_energietraeger_dict(self, j: NEAJahr, s: NEASektor):
        return {d.energietraeger: d.series for d in self.__data if d.jahr == j and d.sektor == s}

    def __create_sektor_dict(self, j: NEAJahr):
        return {sektor: self.__create_energietraeger_dict(j, sektor) for sektor in self.__sektoren}

    def create_dict(self, jahre: list[NEAJahr]):
        return NEAAbschnittDictionary(self.land, self.__sektoren, self.__bereiche,
                                      {jahr: self.__create_sektor_dict(jahr) for jahr in jahre})
