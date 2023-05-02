from Nutzenergieanalyse.nea_bereich import NEABereich


class NEABereicheFactory:
    def create(self):
        return [NEABereich('Raumklima und Warmwasser'),
                NEABereich('Prozesswärme <200 °C'),
                NEABereich('Prozesswärme >200 °C'),
                NEABereich('Standmotoren'),
                NEABereich('Verkehr'),
                NEABereich('Beleuchtung und EDV'),
                NEABereich('Elektrochemie')]
