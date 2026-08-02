from backend.knowledgebase.csv_loader import CSVLoader


class EducationLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Education/degrees.csv"
        )