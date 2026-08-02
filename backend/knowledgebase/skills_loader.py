from backend.knowledgebase.csv_loader import CSVLoader


class SkillsLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/Skills/skills.csv"
        )