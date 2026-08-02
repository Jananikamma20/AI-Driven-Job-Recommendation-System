from backend.knowledgebase.csv_loader import CSVLoader


class CompanyLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Companies/companies.csv"
        )