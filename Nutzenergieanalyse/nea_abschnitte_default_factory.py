from Domain.General import GData
from Domain.Nutzenergieanalyse import NEAAbschnitt, NEAJahr, NEAEnergietraeger, NEAAbschnitteFactory, NEASektor, \
    NEABereich


class NEAAbschnitteDefaultFactory(NEAAbschnitteFactory):
    def create(self, g_data: GData) -> list[NEAAbschnitt]:
        bereiche = g_data.bereiche

        bereiche_default = [NEABereich('Raumklima und Warmwasser', bereiche['Heizen']),
                            NEABereich('Prozesswärme <200 °C', bereiche['Strom']),
                            NEABereich('Prozesswärme >200 °C', bereiche['Warmwasser und Kochen']),
                            NEABereich('Standmotoren', bereiche['Strom']),
                            NEABereich('Verkehr', bereiche['Strom']),
                            NEABereich('Beleuchtung und EDV', bereiche['Strom']),
                            NEABereich('Elektrochemie', bereiche['Strom'])]

        add_bereiche_default = [NEABereich('Kochen', bereiche['Kochen']), NEABereich('Warmwasser', bereiche['Warmwasser'])]

        bereiche_haushalte_ab_2005 = [NEABereich('Raumwärme', bereiche['Heizen']),
                                      NEABereich('Warmwasser', bereiche['Warmwasser']),
                                      NEABereich('Kochen', bereiche['Kochen']),
                                      NEABereich('Kühlen und Gefrieren', bereiche['Strom']),
                                      NEABereich('Großgeräte', bereiche['Strom']),
                                      NEABereich('Haushalts-kleingeräte', bereiche['Strom']),
                                      NEABereich('Büro- und Unter-haltungselektronik', bereiche['Strom']),
                                      NEABereich('Beleuchtung', bereiche['Strom']),
                                      NEABereich('Sonstiges', bereiche['Strom']),
                                      NEABereich('Verkehr', bereiche['Strom'])]

        add_bereiche_haushalte_ab_2005 = [NEABereich('Warmwasser und Kochen', bereiche['Warmwasser und Kochen'])]

        sektoren = g_data.sektoren

        sektoren_vor_2005 = [NEASektor('Wohngebäude', 602, 'A:H', bereiche_default, add_bereiche_default, sektoren['Wohngebäude']),
                             NEASektor('Dienstleistungsgebäude', 576, 'A:H', bereiche_default, add_bereiche_default,
                                       sektoren['Dienstleistungsgebäude']),
                             NEASektor('Landwirtschaftsgebäude', 628, 'A:H', bereiche_default, add_bereiche_default,
                                       sektoren['Landwirtschaftsgebäude'])]

        sektoren_ab_2005 = [
            NEASektor('Wohngebäude', 602, 'U:AE', bereiche_haushalte_ab_2005, add_bereiche_haushalte_ab_2005, sektoren['Wohngebäude']),
            NEASektor('Dienstleistungsgebäude', 576, 'A:H', bereiche_default, add_bereiche_default,
                      sektoren['Dienstleistungsgebäude']),
            NEASektor('Landwirtschaftsgebäude', 628, 'A:H', bereiche_default, add_bereiche_default,
                      sektoren['Landwirtschaftsgebäude'])]

        energietraeger = g_data.energietraeger

        et_vor_1999 = [NEAEnergietraeger('Braunkohle', energietraeger['Braunkohle']),
                       NEAEnergietraeger('Braunkohlenbriketts', energietraeger['Braunkohlen-Briketts']),
                       NEAEnergietraeger('Brenntorf', energietraeger['Brenntorf']),
                       NEAEnergietraeger('Koks', energietraeger['Koks']),
                       NEAEnergietraeger('Steinkohle', energietraeger['Steinkohle']),
                       NEAEnergietraeger('Benzin', energietraeger['Benzin']),
                       NEAEnergietraeger('Gasöl (Diesel)', energietraeger['Diesel']),
                       NEAEnergietraeger('Gasöl für Heizzwecke', energietraeger['Heiz-Gasöl']),
                       NEAEnergietraeger('Leucht- und Flugpetroleum', energietraeger['Petroleum']),
                       NEAEnergietraeger('Heizöl', energietraeger['Heizöl']),
                       NEAEnergietraeger('Flüssiggas', energietraeger['Flüssiggas']),
                       NEAEnergietraeger('Erdgas', energietraeger['Erdgas']),
                       # NEAEnergietraeger('', energietraeger['Mischgas']),
                       NEAEnergietraeger('Brennbare Abfälle', energietraeger['Brennbare Abfälle']),
                       NEAEnergietraeger('Scheitholz', energietraeger['Scheitholz']),
                       NEAEnergietraeger('Biogene Brenn- und Treibstoffe', energietraeger['Biogene']),
                       NEAEnergietraeger('Umgebungswärme etc.', energietraeger['Erneuerbare']),
                       NEAEnergietraeger('Fernwärme', energietraeger['Fernwärme']),
                       NEAEnergietraeger('Elektrische Energie', energietraeger['Elektrische Energie'])]

        et_ab_1999 = [NEAEnergietraeger('Braunkohle', energietraeger['Braunkohle']),
                      # NEAEnergietraeger('', energietraeger['Braunkohlen-Briketts']),
                      NEAEnergietraeger('Brenntorf', energietraeger['Brenntorf']),
                      NEAEnergietraeger('Koks', energietraeger['Koks']),
                      # NEAEnergietraeger('Petrolkoks', energietraeger['Koks']),
                      NEAEnergietraeger('Steinkohle', energietraeger['Steinkohle']),
                      NEAEnergietraeger('Benzin', energietraeger['Benzin']),
                      NEAEnergietraeger('Diesel', energietraeger['Diesel']),
                      NEAEnergietraeger('Gasöl für Heizzwecke', energietraeger['Heiz-Gasöl']),
                      NEAEnergietraeger('Petroleum', energietraeger['Petroleum']),
                      NEAEnergietraeger('Heizöl', energietraeger['Heizöl']),
                      NEAEnergietraeger('Flüssiggas', energietraeger['Flüssiggas']),
                      NEAEnergietraeger('Erdgas', energietraeger['Erdgas']),
                      # NEAEnergietraeger('', energietraeger['Mischgas']),
                      NEAEnergietraeger('Brennbare Abfälle', energietraeger['Brennbare Abfälle']),
                      NEAEnergietraeger('Scheitholz', energietraeger['Scheitholz']),
                      NEAEnergietraeger('Biogene Brenn- und Treibstoffe', energietraeger['Biogene']),
                      NEAEnergietraeger('Umgebungswärme etc.', energietraeger['Erneuerbare']),
                      NEAEnergietraeger('Fernwärme', energietraeger['Fernwärme']),
                      NEAEnergietraeger('Elektrische Energie', energietraeger['Elektrische Energie'])]

        return [NEAAbschnitt('vor_1999',
                             [NEAJahr('NEA 93', '1993'),
                              NEAJahr('NEA 94', '1994'),
                              NEAJahr('NEA 95', '1995'),
                              NEAJahr('NEA 96', '1996'),
                              NEAJahr('NEA 97', '1997'),
                              NEAJahr('NEA 98', '1998')],
                             sektoren_vor_2005,
                             et_vor_1999),
                NEAAbschnitt('1999_bis_2004',
                             [NEAJahr('NEA 99', '1999'),
                              NEAJahr('NEA 2000', '2000'),
                              NEAJahr('NEA 2001', '2001'),
                              NEAJahr('NEA 2002', '2002'),
                              NEAJahr('NEA 2003', '2003'),
                              NEAJahr('NEA 2004', '2004')],
                             sektoren_vor_2005,
                             et_ab_1999),
                NEAAbschnitt('ab_2005',
                             [NEAJahr('NEA 2005', '2005'),
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
                             sektoren_ab_2005,
                             et_ab_1999)]
