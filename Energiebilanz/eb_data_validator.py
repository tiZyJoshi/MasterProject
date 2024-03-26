from Domain.Energiebilanz import EBLand, EBSektor, EBData


class EBDataValidator:
    def create_total_sum(self, data: EBData):
        return sum(sum(data.data[land][sektor] for sektor in data.data[land].keys()) for land in data.data.keys())
