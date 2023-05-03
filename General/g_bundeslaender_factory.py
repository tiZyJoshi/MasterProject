from Domain.General import GLand, GLaenderFactory


class GBundeslaenderFactory(GLaenderFactory):
    def create(self) -> dict[str, GLand]:
        laender = [GLand('burgenland'),
                   GLand('kaernten'),
                   GLand('niederoesterreich'),
                   GLand('oberoesterreich'),
                   GLand('salzburg'),
                   GLand('steiermark'),
                   GLand('tirol'),
                   GLand('vorarlberg'),
                   GLand('wien')]
        return {land.name: land for land in laender}
