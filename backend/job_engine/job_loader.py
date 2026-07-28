import pandas as pd


class JobLoader:

    def __init__(self):

        pass

    def load(self, csv_path):

        dataframe = pd.read_csv(csv_path)

        return dataframe