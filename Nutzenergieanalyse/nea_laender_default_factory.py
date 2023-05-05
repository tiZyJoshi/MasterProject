from Domain.General import GLand
from Domain.Nutzenergieanalyse import NEALaenderFactory, NEALand


class NEALaenderDefaultFactory(NEALaenderFactory):
    def create(self, laender: dict[str, GLand]) -> list[NEALand]:
        return list([NEALand(land.name, land) for land in laender.values()])
