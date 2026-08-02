from backend.knowledgebase.csv_loader import CSVLoader


class TechnologyLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Technologies/technologies.csv"
        )