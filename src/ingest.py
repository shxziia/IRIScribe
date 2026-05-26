import pandas as pd


def load_csv(path):

    data = pd.read_csv(path)

    return data