from Domain.General import GLand
from Domain.Energiebilanz import EBLand


class EBLaenderFactory:
    def create(self, laender: dict[str, GLand]) -> list[EBLand]:
        pass
