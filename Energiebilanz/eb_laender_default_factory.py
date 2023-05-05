from Domain.General import GLand
from Domain.Energiebilanz import EBLaenderFactory, EBLand


class EBLaenderDefaultFactory(EBLaenderFactory):
    def create(self, laender: dict[str, GLand]) -> list[EBLand]:
        return list([EBLand(land.name, land) for land in laender.values()])
