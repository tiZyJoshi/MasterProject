from Nutzenergieanalyse.nea_land import NEALand


class NEALaender:
    def __init__(self, laender: list[NEALand]):
        self.laender = laender
        self.oesterreich = 'oesterreich'

    def get_bundeslaender(self) -> list[NEALand]:
        return list(filter(lambda land: land.name != self.oesterreich, self.laender))

    def get_oesterreich(self) -> list[NEALand]:
        return list(filter(lambda land: land.name == self.oesterreich, self.laender))
