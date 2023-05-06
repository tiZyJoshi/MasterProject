from Domain.Nutzenergieanalyse import NEABereich, NEABereicheFactory, NEABereichKlasse


class NEABereicheDefaultFactory(NEABereicheFactory):
    def __init__(self, klassen: dict[str, NEABereichKlasse]):
        self.__klassen = klassen

    def create(self) -> list[NEABereich]:
        return [NEABereich('Raumklima und Warmwasser', 'Raumklima und Warmwasser', self.__klassen['Heizen']),
                NEABereich('Prozesswärme <200 °C', 'Prozesswärme l200 °C', self.__klassen['Strom']),
                NEABereich('Prozesswärme >200 °C', 'Prozesswärme h200 °C', self.__klassen['Warmwasser']),
                NEABereich('Standmotoren', 'Standmotoren', self.__klassen['Strom']),
                NEABereich('Verkehr', 'Verkehr', self.__klassen['Strom']),
                NEABereich('Beleuchtung und EDV', 'Beleuchtung und EDV', self.__klassen['Strom']),
                NEABereich('Elektrochemie', 'Elektrochemie', self.__klassen['Strom'])]
