import pandas as pd

from .df_extension import DFExtension
from .df_extrapolation import DFExtrapolation
from .df_nan_extension import DFNanExtension


class DFExtrapolationExtension(DFExtension):
    def __init__(self, extrapolation: DFExtrapolation):
        self.__extrapolation = extrapolation
        self.__nanExtension = DFNanExtension()

    def run(self, df: pd.DataFrame, index: pd.PeriodIndex) -> pd.DataFrame:
        extension = self.__nanExtension.run(df, index)
        extrapolation = self.__extrapolation.run(extension)
        return extrapolation
