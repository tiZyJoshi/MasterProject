from Domain.General import GLand, GLaenderFactory


class GOesterreichFactory(GLaenderFactory):
    def create(self) -> dict[str, GLand]:
        laender = [GLand('oesterreich')]
        return {land.name: land for land in laender}
