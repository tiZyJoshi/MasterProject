from Domain.Nutzenergieanalyse import NEABereich, NEABereicheFactory


class NEABereicheDefaultFactory(NEABereicheFactory):
    def create(self) -> list[NEABereich]:
        return [NEABereich('Raumklima und Warmwasser'),
                NEABereich('Prozesswärme <200 °C'),
                NEABereich('Prozesswärme >200 °C'),
                NEABereich('Standmotoren'),
                NEABereich('Verkehr'),
                NEABereich('Beleuchtung und EDV'),
                NEABereich('Elektrochemie')]
