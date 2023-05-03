from Domain.Nutzenergieanalyse import NEAAbschnitt, NEALand, NEASektor, NEAData


class NEADataValidator:
    @staticmethod
    def __create_sektor_sum(land: NEALand, abschnitt: NEAAbschnitt, sektor: NEASektor, data: NEAData):
        return sum(data.data[land][abschnitt][sektor][bereich] for bereich in data.bereiche)

    def __create_sektor_sums(self, land: NEALand, abschnitt: NEAAbschnitt, data: NEAData):
        return {sektor: self.__create_sektor_sum(land, abschnitt, sektor, data) for sektor in data.sektoren}

    @staticmethod
    def __create_sektor_total_sum(sektor_sums, data: NEAData):
        return sum(sektor_sums[sektor] for sektor in data.sektoren[0:3])

    def __create_abschnitt_sum(self, land: NEALand, abschnitt: NEAAbschnitt, data: NEAData):
        sector_sums = self.__create_sektor_sums(land, abschnitt, data)
        return self.__create_sektor_total_sum(sector_sums, data)

    def create_laender_sum(self, laender: list[NEALand], data: NEAData):
        return {abschnitt: sum(self.__create_abschnitt_sum(land, abschnitt, data) for land in laender) for
                abschnitt in data.abschnitte}

    def create_total_sum(self, data: NEAData):
        return self.create_laender_sum(data.laender, data)
