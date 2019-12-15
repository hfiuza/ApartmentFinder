import pandas as pd

import os

from constants import LOCAL_PATH, APARTMENTS_FILENAME


def basic_write(df):
    df.to_csv(os.path.join(LOCAL_PATH, APARTMENTS_FILENAME))


def basic_read():
    return pd.read_csv(os.path.join(LOCAL_PATH, APARTMENTS_FILENAME))
