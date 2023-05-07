from Domain.General import GEnergietraegerKlassenFactory, GEnergietraegerKlasse


class GEnergietraegerKlassenSimpleFactory(GEnergietraegerKlassenFactory):
    def create(self) -> dict[str, GEnergietraegerKlasse]:
        klassen = [GEnergietraegerKlasse('Fossile fest'),
                   GEnergietraegerKlasse('Fossile flüssig'),
                   GEnergietraegerKlasse('Fossile gasförmig'),
                   GEnergietraegerKlasse('Brennbare Abfälle'),
                   GEnergietraegerKlasse('Scheitholz'),
                   GEnergietraegerKlasse('Biogene'),
                   GEnergietraegerKlasse('Erneuerbare'),
                   GEnergietraegerKlasse('Fernwärme'),
                   GEnergietraegerKlasse('Elektrische Energie')]
        return {klasse.name: klasse for klasse in klassen}
