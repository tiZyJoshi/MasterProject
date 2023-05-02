from dataclasses import dataclass

from Nutzenergieanalyse.nea_bereich import NEABereich
from Nutzenergieanalyse.nea_energietraeger import NEAEnergietraeger
from Nutzenergieanalyse.nea_jahr import NEAJahr
from Nutzenergieanalyse.nea_land import NEALand
from Nutzenergieanalyse.nea_sektor import NEASektor
from Nutzenergieanalyse.nea_typ import NEATyp


@dataclass
class NEAAbschnitt:
    name: str
    jahre: list[NEAJahr]
    energietraeger: list[NEAEnergietraeger]

    def __hash__(self):
        return hash(self.name)


def plot_nea_differences(dataframes, bundeslaender: list[NEALand], oesterreich: list[NEALand],
                         abschnitte: list[NEAAbschnitt], sektoren: list[NEASektor], bereiche: list[NEABereich]):
    bl_sum = create_nea_laender_sum(dataframes, bundeslaender, abschnitte, sektoren, bereiche)
    at_sum = create_nea_laender_sum(dataframes, oesterreich, abschnitte, sektoren, bereiche)
    for abschnitt in abschnitte:
        (at_sum[abschnitt] - bl_sum[abschnitt]).plot()


def create_nea_typen():
    return [NEATyp('energiegesamtrechnungskonform', 'A:H')]


def create_nea_typen_ab_2005():
    return [NEATyp('energiegesamtrechnungskonform', 'A:H')]