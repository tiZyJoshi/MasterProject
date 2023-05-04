from Domain.Nutzenergieanalyse import NEABereich, NEABereicheFactory


class NEABereicheDefaultFactory(NEABereicheFactory):
    def create(self) -> list[NEABereich]:
        return [NEABereich('Raumklima und Warmwasser', 'Raumklima und Warmwasser'),
                NEABereich('Prozesswärme <200 °C', 'Prozesswärme l200 °C'),
                NEABereich('Prozesswärme >200 °C', 'Prozesswärme h200 °C'),
                NEABereich('Standmotoren', 'Standmotoren'),
                NEABereich('Verkehr', 'Verkehr'),
                NEABereich('Beleuchtung und EDV', 'Beleuchtung und EDV'),
                NEABereich('Elektrochemie', 'Elektrochemie')]
