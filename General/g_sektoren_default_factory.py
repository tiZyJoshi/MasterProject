from Domain.General import GSektor, GSektorenFactory


class GSektorenDefaultFactory(GSektorenFactory):
    def create(self) -> dict[str, GSektor]:
        sektoren = [GSektor('Wohngebäude'),
                    GSektor('Dienstleistungsgebäude'),
                    GSektor('Landwirtschaftsgebäude')]
        return {sektor.name: sektor for sektor in sektoren}
