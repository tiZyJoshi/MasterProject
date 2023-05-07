from Domain.General import GData

from .eb_energietraeger import EBEnergietraeger


class EBEnergietraegerFactory:
    def create(self, g_data: GData) -> list[EBEnergietraeger]:
        pass
