import pandas as pd

from Domain.Energiebilanz import EBSektor, EBFile, EBEnergietraeger
from Domain.Energiebilanz.eb_datafield import EBDataField
from Energiebilanz.eb_file_data_factory import EBFileDataFactory


class EBFileDataDefaultFactory(EBFileDataFactory):
    @staticmethod
    def __create_empty_data(sektoren: list[EBSektor]):
        index = pd.period_range('1988', '2020', freq='A')
        for sektor in sektoren:
            yield pd.Series((0 for i in index), index, name=sektor.name)

    def __load(self, file: EBFile, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]):
        with pd.ExcelFile(file.path) as xls:
            for et in energietraeger:
                print(f'Starting {et}')
                if et.name not in xls.sheet_names:
                    print(f'{et} missing')
                    continue
                raw_data = pd.read_excel(xls,
                                         sheet_name=et.name,
                                         header=0,
                                         index_col=0,
                                         skiprows=408,
                                         nrows=21)

                local_df = raw_data.filter(items=list(s.name for s in sektoren), axis=0)
                local_df = local_df.swapaxes("index", "columns")
                local_df = local_df.filter(items=list(n for n in local_df.index if type(n) == int), axis=0)

                x, y = local_df.shape
                if len(local_df) == 0 or x == 0 or y == 0:
                    print(f'{et} empty')
                    local_df = pd.concat(self.__create_empty_data(sektoren), axis=1)

                local_df.index = pd.PeriodIndex(local_df.index, freq='A', name=et.name)

                for sektor in sektoren:
                    series = local_df[sektor.name]
                    series.name = et.name
                    yield EBDataField(sektor, et, series)

    def create(self, file: EBFile, energietraeger: list[EBEnergietraeger], sektoren: list[EBSektor]) -> \
            list[EBDataField]:
        return list(self.__load(file, energietraeger, sektoren))
