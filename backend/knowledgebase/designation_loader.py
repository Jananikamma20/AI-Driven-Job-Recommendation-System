from backend.knowledgebase.csv_loader import CSVLoader


class DesignationLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Designations/designations.csv"
        )