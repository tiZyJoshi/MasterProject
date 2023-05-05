from Domain.General import GEnergietraeger
from Domain.Nutzenergieanalyse import NEAAbschnitt, NEAJahr, NEAEnergietraeger, NEAAbschnitteFactory


class NEAAbschnitteDefaultFactory(NEAAbschnitteFactory):
    def __init__(self, energietraeger: dict[str, GEnergietraeger]):
        self.__energietraeger = energietraeger

    def create(self) -> list[NEAAbschnitt]:
        return [NEAAbschnitt('vor_1999',
                             [NEAJahr('NEA 93', '1993'),
                              NEAJahr('NEA 94', '1994'),
                              NEAJahr('NEA 95', '1995'),
                              NEAJahr('NEA 96', '1996'),
                              NEAJahr('NEA 97', '1997'),
                              NEAJahr('NEA 98', '1998')],
                             [NEAEnergietraeger('Braunkohle', self.__energietraeger['Braunkohle']),
                              NEAEnergietraeger('Braunkohlenbriketts', self.__energietraeger['Braunkohlen-Briketts']),
                              NEAEnergietraeger('Brenntorf', self.__energietraeger['Brenntorf']),
                              NEAEnergietraeger('Koks', self.__energietraeger['Koks']),
                              NEAEnergietraeger('Steinkohle', self.__energietraeger['Steinkohle']),
                              NEAEnergietraeger('Benzin', self.__energietraeger['Benzin']),
                              NEAEnergietraeger('Gasöl (Diesel)', self.__energietraeger['Diesel']),
                              NEAEnergietraeger('Gasöl für Heizzwecke', self.__energietraeger['Heiz-Gasöl']),
                              NEAEnergietraeger('Leucht- und Flugpetroleum', self.__energietraeger['Petroleum']),
                              NEAEnergietraeger('Heizöl', self.__energietraeger['Heizöl']),
                              NEAEnergietraeger('Flüssiggas', self.__energietraeger['Flüssiggas']),
                              NEAEnergietraeger('Erdgas', self.__energietraeger['Erdgas']),
                              # NEAEnergietraeger('', self.__energietraeger['Mischgas']),
                              NEAEnergietraeger('Brennbare Abfälle', self.__energietraeger['Brennbare Abfälle']),
                              NEAEnergietraeger('Scheitholz', self.__energietraeger['Scheitholz']),
                              NEAEnergietraeger('Biogene Brenn- und Treibstoffe', self.__energietraeger['Biogene']),
                              NEAEnergietraeger('Umgebungswärme etc.', self.__energietraeger['Erneuerbare']),
                              NEAEnergietraeger('Fernwärme', self.__energietraeger['Fernwärme']),
                              NEAEnergietraeger('Elektrische Energie', self.__energietraeger['Elektrische Energie'])]),
                NEAAbschnitt('ab_1999',
                             [NEAJahr('NEA 99', '1999'),
                              NEAJahr('NEA 2000', '2000'),
                              NEAJahr('NEA 2001', '2001'),
                              NEAJahr('NEA 2002', '2002'),
                              NEAJahr('NEA 2003', '2003'),
                              NEAJahr('NEA 2004', '2004'),
                              NEAJahr('NEA 2005', '2005'),
                              NEAJahr('NEA 2006', '2006'),
                              NEAJahr('NEA 2007', '2007'),
                              NEAJahr('NEA 2008', '2008'),
                              NEAJahr('NEA 2009', '2009'),
                              NEAJahr('NEA 2010', '2010'),
                              NEAJahr('NEA 2011', '2011'),
                              NEAJahr('NEA 2012', '2012'),
                              NEAJahr('NEA 2013', '2013'),
                              NEAJahr('NEA 2014', '2014'),
                              NEAJahr('NEA 2015', '2015'),
                              NEAJahr('NEA 2016', '2016'),
                              NEAJahr('NEA 2017', '2017'),
                              NEAJahr('NEA 2018', '2018'),
                              NEAJahr('NEA 2019', '2019'),
                              NEAJahr('NEA 2020', '2020')],
                             [NEAEnergietraeger('Braunkohle', self.__energietraeger['Braunkohle']),
                              # NEAEnergietraeger('', self.__energietraeger['Braunkohlen-Briketts']),
                              NEAEnergietraeger('Brenntorf', self.__energietraeger['Brenntorf']),
                              NEAEnergietraeger('Koks', self.__energietraeger['Koks']),
                              # NEAEnergietraeger('Petrolkoks', self.__energietraeger['Koks']),
                              NEAEnergietraeger('Steinkohle', self.__energietraeger['Steinkohle']),
                              NEAEnergietraeger('Benzin', self.__energietraeger['Benzin']),
                              NEAEnergietraeger('Diesel', self.__energietraeger['Diesel']),
                              NEAEnergietraeger('Gasöl für Heizzwecke', self.__energietraeger['Heiz-Gasöl']),
                              NEAEnergietraeger('Petroleum', self.__energietraeger['Petroleum']),
                              NEAEnergietraeger('Heizöl', self.__energietraeger['Heizöl']),
                              NEAEnergietraeger('Flüssiggas', self.__energietraeger['Flüssiggas']),
                              NEAEnergietraeger('Erdgas', self.__energietraeger['Erdgas']),
                              # NEAEnergietraeger('', self.__energietraeger['Mischgas']),
                              NEAEnergietraeger('Brennbare Abfälle', self.__energietraeger['Brennbare Abfälle']),
                              NEAEnergietraeger('Scheitholz', self.__energietraeger['Scheitholz']),
                              NEAEnergietraeger('Biogene Brenn- und Treibstoffe', self.__energietraeger['Biogene']),
                              NEAEnergietraeger('Umgebungswärme etc.', self.__energietraeger['Erneuerbare']),
                              NEAEnergietraeger('Fernwärme', self.__energietraeger['Fernwärme']),
                              NEAEnergietraeger('Elektrische Energie', self.__energietraeger['Elektrische Energie'])])]
