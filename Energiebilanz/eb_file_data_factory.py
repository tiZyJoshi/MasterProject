from Domain.Energiebilanz import EBFile, EBEnergietraeger, EBSektor
from Domain.Energiebilanz.eb_datafield import EBDataField


class EBFileDataFactory:
    def create(self, file: EBFile, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]) -> \
            list[EBDataField]:
        pass
