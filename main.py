# This is a sample Python script.
from Domain.General import GLand, GEnergietraeger, GEnergietraegerKlasse, GSektor
from Domain.Nutzenergieanalyse import NEALand, NEAAbschnitt, NEASektor, NEABereich, NEATyp


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def plot_nea_differences(dataframes, bundeslaender: list[NEALand], oesterreich: list[NEALand],
                         abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor], bereiche: list[NEABereich]):
    # bl_sum = create_nea_laender_sum(dataframes, bundeslaender, abschnitte, sektoren, bereiche)
    # at_sum = create_nea_laender_sum(dataframes, oesterreich, abschnitte, sektoren, bereiche)
    # for abschnitt in abschnitte:
    #    (at_sum[abschnitt] - bl_sum[abschnitt]).plot()
    pass


def create_nea_typen():
    return [NEATyp('energiegesamtrechnungskonform', 'A:H')]


def create_nea_typen_ab_2005():
    return [NEATyp('energiegesamtrechnungskonform', 'A:H')]
