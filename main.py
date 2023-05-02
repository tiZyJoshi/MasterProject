# This is a sample Python script.
from General.GLand import GLand
from General.GEnergietraeger import GEnergietraeger
from General.GEnergietraegerKlasse import GEnergietraegerKlasse
from General.GSektor import GSektor


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def create_laender_dict():
    laender = [GLand('oesterreich'),
               GLand('burgenland'),
               GLand('kaernten'),
               GLand('niederoesterreich'),
               GLand('oberoesterreich'),
               GLand('salzburg'),
               GLand('steiermark'),
               GLand('tirol'),
               GLand('vorarlberg'),
               GLand('wien')]
    return {land.name: land for land in laender}


def create_sektoren_dict():
    sektoren = [GSektor('Wohngebäude'),
                GSektor('Dienstleistungsgebäude'),
                GSektor('Landwirtschaftsgebäude')]
    return {sektor.name: sektor for sektor in sektoren}


def create_entergietraeger_klassen_dict():
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


def create_energietraeger_dict(klassen):
    energietraeger_list = [GEnergietraeger('Braunkohle', klassen['Fossile fest']),
                           GEnergietraeger('Braunkohlen-Briketts', klassen['Fossile fest']),
                           GEnergietraeger('Brenntorf', klassen['Fossile fest']),
                           GEnergietraeger('Koks', klassen['Fossile fest']),
                           GEnergietraeger('Steinkohle', klassen['Fossile fest']),
                           GEnergietraeger('Benzin', klassen['Fossile flüssig']),
                           GEnergietraeger('Diesel', klassen['Fossile flüssig']),
                           GEnergietraeger('Heiz-Gasöl', klassen['Fossile flüssig']),
                           GEnergietraeger('Petroleum', klassen['Fossile flüssig']),
                           GEnergietraeger('Heizöl', klassen['Fossile flüssig']),
                           GEnergietraeger('Flüssiggas', klassen['Fossile flüssig']),
                           GEnergietraeger('Erdgas', klassen['Fossile gasförmig']),
                           GEnergietraeger('Mischgas', klassen['Fossile gasförmig']),
                           GEnergietraeger('Brennbare Abfälle', klassen['Brennbare Abfälle']),
                           GEnergietraeger('Scheitholz', klassen['Scheitholz']),
                           GEnergietraeger('Biogene', klassen['Biogene']),
                           GEnergietraeger('Erneuerbare', klassen['Erneuerbare']),
                           GEnergietraeger('Fernwärme', klassen['Fernwärme']),
                           GEnergietraeger('Elektrische Energie', klassen['Elektrische Energie'])]
    return {energietraeger.name: energietraeger for energietraeger in energietraeger_list}


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
