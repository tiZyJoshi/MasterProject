import pandas as pd

from .df_extension import DFExtension


class DFNanExtension(DFExtension):
    def run(self, df: pd.DataFrame, index: pd.PeriodIndex) -> pd.DataFrame:
        return pd.DataFrame(df, index, copy=True)
