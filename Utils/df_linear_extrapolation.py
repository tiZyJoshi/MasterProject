import pandas as pd

from .df_extrapolation import DFExtrapolation


class DFLinearExtrapolation(DFExtrapolation):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        copy = df.copy()
        for col in copy.columns:
            # Extract column
            ser = copy[col].copy()

            # End piece
            increment = ser.diff(1).mean()
            idx_max_notna = ser[ser.notna()].index.array[-1]
            idx = ser.index[ser.index >= idx_max_notna]
            ser[idx] = ser[idx].fillna(increment).cumsum()

            # Start piece
            ser = pd.Series(ser.array[::-1])
            increment = ser.diff(1).mean()
            idx_max_notna = ser[ser.notna()].index.array[-1]
            idx = ser.index[ser.index >= idx_max_notna]
            ser[idx] = ser[idx].fillna(increment).cumsum()
            copy[col] = ser.array[::-1]
        return copy


class DFSARIMAXExtrapolation(DFExtrapolation):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        copy = df.copy()
        for col in copy.columns:
            # Extract column
            ser = copy[col].copy()

            # End piece
            increment = ser.diff(1).mean()
            idx_max_notna = ser[ser.notna()].index.array[-1]
            idx = ser.index[ser.index >= idx_max_notna]
            ser[idx] = ser[idx].fillna(increment).cumsum()

            # Start piece
            ser = pd.Series(ser.array[::-1])
            increment = ser.diff(1).mean()
            idx_max_notna = ser[ser.notna()].index.array[-1]
            idx = ser.index[ser.index >= idx_max_notna]
            ser[idx] = ser[idx].fillna(increment).cumsum()
            copy[col] = ser.array[::-1]
        return copy
