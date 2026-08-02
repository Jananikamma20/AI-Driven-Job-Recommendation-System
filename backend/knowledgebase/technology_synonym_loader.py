from backend.knowledgebase.csv_loader import CSVLoader


class TechnologySynonymLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Synonyms/technology_synonyms.csv"
        )