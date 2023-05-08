import pandas as pd

from Domain.Nutzenergieanalyse import NEAData, NEADataFactory
from Domain.General import GLand, GSektor, GData, GEnergietraegerKlasse, GEnergietraeger


def create_series(df: pd.DataFrame, et_klasse: GEnergietraegerKlasse, ets: list[GEnergietraeger]):
    klassen_ets = [et for et in ets if et.klasse == et_klasse]
    series = [df[et.name].fillna(0) for et in klassen_ets]
    return pd.Series(sum(series), df.index, name=et_klasse.name)


def sum_et_klassen(dataframe: pd.DataFrame, g_data: GData):
    ets = list([g_data.energietraeger[et] for et in dataframe.columns.values])
    s = [create_series(dataframe, et_klasse, ets) for et_klasse in g_data.energietraeger_klassen.values()]
    return pd.concat(s, axis=1)


def create_bereiche_dict(data, land: GLand, sektor: GSektor, g_data: GData):
    return {bereich: sum_et_klassen(data[land][sektor][bereich], g_data) for bereich in data[land][sektor].keys()}


def create_sektor_dict(data, land: GLand, g_data: GData):
    return {sektor: create_bereiche_dict(data, land, sektor, g_data) for sektor in data[land].keys()}


class NEADataETKlassenFactory(NEADataFactory):
    def __init__(self, data_factory: NEADataFactory):
        self.__data_factory = data_factory

    def create(self, g_data: GData) -> NEAData:
        data = self.__data_factory.create(g_data).data
        return NEAData({land: create_sektor_dict(data, land, g_data) for land in data.keys()})
