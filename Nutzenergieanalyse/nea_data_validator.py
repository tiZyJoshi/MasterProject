from Nutzenergieanalyse.nea_abschnitt import NEAAbschnitt
from Nutzenergieanalyse.nea_data import NEAData
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor


class NEADataValidator:
    def __init__(self, data: NEAData):
        self.__data = data

    def __create_sektor_sum(self, land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor):
        return sum(self.__data.get(land, abschnitt, sektor, bereich) for bereich in self.__data.bereiche)

    def __create_sektor_sums(self, land: NEALand, abschnitt: NEAAbschnitt):
        return {sektor: self.__create_sektor_sum(land, abschnitt, sektor) for sektor in self.__data.sektoren}

    def __create_sektor_total_sum(self, sektor_sums):
        return sum(sektor_sums[sektor] for sektor in self.__data.sektoren[0:3])

    def __create_abschnitt_sum(self, land: NEALand, abschnitt: NEAAbschnitt):
        sector_sums = self.__create_sektor_sums(land, abschnitt)
        return self.__create_sektor_total_sum(sector_sums)

    def create_laender_sum(self, laender: list[NEALand]):
        return {abschnitt: sum(self.__create_abschnitt_sum(land, abschnitt) for land in laender) for
                abschnitt in self.__data.abschnitte}

    def create_total_sum(self):
        return self.create_laender_sum(self.__data.laender)
