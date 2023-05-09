import pandas as pd

from Domain.Energiebilanz import EBDataFactory, EBData
from Domain.General import GLand, GData, GEnergietraegerKlasse, GEnergietraeger


def create_series(df: pd.DataFrame, et_klasse: GEnergietraegerKlasse, ets: list[GEnergietraeger]):
    klassen_ets = [et for et in ets if et.klasse == et_klasse]
    series = [df[et.name].fillna(0) for et in klassen_ets]
    return pd.Series(sum(series), df.index, name=et_klasse.name)


def sum_et_klassen(dataframe: pd.DataFrame, g_data: GData):
    ets = list([g_data.energietraeger[et] for et in dataframe.columns.values])
    s = [create_series(dataframe, et_klasse, ets) for et_klasse in g_data.energietraeger_klassen.values()]
    return pd.concat(s, axis=1)


def create_sektor_dict(data, land: GLand, g_data: GData):
    return {sektor: sum_et_klassen(data[land][sektor], g_data) for sektor in data[land].keys()}


class EBDataETKlassenFactory(EBDataFactory):
    def __init__(self, data_factory: EBDataFactory):
        self.__data_factory = data_factory

    def create(self, g_data: GData) -> EBData:
        data = self.__data_factory.create(g_data).data
        return EBData({land: create_sektor_dict(data, land, g_data) for land in data.keys()})
