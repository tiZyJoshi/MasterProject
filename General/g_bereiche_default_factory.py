from Domain.General import GBereich, GBereicheFactory


class GBereicheDefaultFactory(GBereicheFactory):
    def create(self) -> dict[str, GBereich]:
        bereiche_list = [GBereich('Warmwasser'),
                         GBereich('Heizen'),
                         GBereich('Kochen'),
                         GBereich('Warmwasser und Kochen'),
                         GBereich('Strom')]
        return {bereich.name: bereich for bereich in bereiche_list}
