import pandas as pd


class CSVLoader:

    def load(self, path):

        try:

            df = pd.read_csv(path)

            return df

        except Exception as e:

            print(f"Error loading {path}")

            print(e)

            return pd.DataFrame()