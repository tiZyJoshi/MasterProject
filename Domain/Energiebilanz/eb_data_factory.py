from .eb_data import EBData
from .eb_energietraeger import EBEnergietraeger
from .eb_sektor import EBSektor


class EBDataFactory:
    def create(self, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]) -> EBData:
        pass
