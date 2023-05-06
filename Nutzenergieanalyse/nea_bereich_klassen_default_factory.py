from Domain.Nutzenergieanalyse import NEABereichKlassenFactory, NEABereichKlasse


class NEABereichKlassenDefaultFactory(NEABereichKlassenFactory):
    def create(self) -> dict[str, NEABereichKlasse]:
        klassen = [NEABereichKlasse('Heizen'),
                   NEABereichKlasse('Strom'),
                   NEABereichKlasse('Warmwasser')]
        return {klasse.name: klasse for klasse in klassen}
