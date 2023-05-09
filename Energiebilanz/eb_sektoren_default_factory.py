from Domain.Energiebilanz import EBSektor, EBSektorenFactory
from Domain.General import GData


class EBSektorenDefaultFactory(EBSektorenFactory):
    def create(self, g_data: GData) -> list[EBSektor]:
        return [EBSektor('Private Haushalte', g_data.sektoren['Wohngebäude']),
                EBSektor('Öffentliche und Private Dienstleistungen', g_data.sektoren['Dienstleistungsgebäude']),
                EBSektor('Landwirtschaft', g_data.sektoren['Landwirtschaftsgebäude'])]
