from Domain.General import GBereicheFactory, GBereich


class GBereicheSimpleFactory(GBereicheFactory):
    def create(self) -> dict[str, GBereich]:
        bereiche_list = [GBereich('Heizen'),
                         GBereich('Warmwasser und Kochen'),
                         GBereich('Strom')]
        return {bereich.name: bereich for bereich in bereiche_list}
