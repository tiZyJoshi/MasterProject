import pandas as pd
import pmdarima as pm
from pmdarima import model_selection

from Utils import DFExtrapolation


class DFSARIMAXExtrapolation(DFExtrapolation):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        copy = df.copy()
        for col in copy.columns:
            ser = copy[col].copy()
            train, test = model_selection.train_test_split(ser['2005':'2020'], train_size=10)
            arima = pm.auto_arima(train, seasonal=False)
            predict = arima.predict(n_periods=26)
            copy[col] = pd.concat([copy[col][:'2020'], predict['2021':] - predict['2021'] + ser['2020']])
        return copy

class DFSARIMAXExtrapolation2(DFExtrapolation):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        copy = df.copy()
        for col in copy.columns:
            ser = copy[col].copy()
            train, test = model_selection.train_test_split(ser['2005':'2020'], train_size=10)
            arima = pm.auto_arima(train, seasonal=False)
            predict = arima.predict(n_periods=26)
            copy[col] = pd.concat([copy[col][:'2020'], predict['2021':] - predict['2021'] + ser['2020']])
        return copy
