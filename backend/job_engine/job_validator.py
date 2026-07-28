class JobValidator:

    def __init__(self):

        pass


    def validate(self, dataframe):

        dataframe = dataframe.drop_duplicates()

        if "title" in dataframe.columns:

            dataframe = dataframe.dropna(

                subset=["title"]

            )

        if "description" in dataframe.columns:

            dataframe = dataframe.dropna(

                subset=["description"]

            )

        dataframe = dataframe.reset_index(

            drop=True

        )

        return dataframe