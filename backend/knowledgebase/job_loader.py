from backend.knowledgebase.csv_loader import CSVLoader


class JobLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Jobs/jobs.csv"
        )