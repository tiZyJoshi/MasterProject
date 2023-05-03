from Domain.General import GEnergietraegerKlasse, GEnergietraegerKlassenFactory


class GEnergietraegerKlassenDefaultFactory(GEnergietraegerKlassenFactory):
    def create(self) -> dict[str, GEnergietraegerKlasse]:
        klassen = [GEnergietraegerKlasse('Fossile fest'),
                   GEnergietraegerKlasse('Fossile flüssig'),
                   GEnergietraegerKlasse('Fossile gasförmig'),
                   GEnergietraegerKlasse('Brennbare Abfälle'),
                   GEnergietraegerKlasse('Scheitholz'),
                   GEnergietraegerKlasse('Biogene'),
                   GEnergietraegerKlasse('Biogene fest'),
                   GEnergietraegerKlasse('Biogene flüssig'),
                   GEnergietraegerKlasse('Biogene gasförmig'),
                   GEnergietraegerKlasse('Erneuerbare'),
                   GEnergietraegerKlasse('Erneuerbare Geothermie'),
                   GEnergietraegerKlasse('Erneuerbare Umweltwärme'),
                   GEnergietraegerKlasse('Erneuerbare Solarwärme'),
                   GEnergietraegerKlasse('Fernwärme'),
                   GEnergietraegerKlasse('Elektrische Energie')]
        return {klasse.name: klasse for klasse in klassen}
