import pandas as pd


class SkillLoader:

    def __init__(self):

        self.skills = []

    def load(self, csv_path):

        dataframe = pd.read_csv(csv_path)

        self.skills = (

            dataframe["skill"]

            .dropna()

            .astype(str)

            .tolist()

        )

        return self.skills