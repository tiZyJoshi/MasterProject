from Domain.Energiebilanz import EBLand, EBSektor, EBData


class EBDataValidator:
    @staticmethod
    def __create_sektor_sum(land: EBLand, sektoren: list[EBSektor], data: EBData):
        return sum(data.data[land][sektor] for sektor in sektoren)

    def __create_laender_sum(self, laender: list[EBLand], sektoren: list[EBSektor], data: EBData):
        return sum(self.__create_sektor_sum(land, sektoren, data) for land in laender)

    def create_total_sum(self, data: EBData):
        return self.__create_laender_sum(data.laender, data.sektoren, data)
