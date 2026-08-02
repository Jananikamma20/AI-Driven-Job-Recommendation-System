from backend.knowledgebase.csv_loader import CSVLoader


class SoftSkillLoader:

    def __init__(self):

        self.loader = CSVLoader()

    def load(self):

        return self.loader.load(
            "Data/KnowledgeBase/SoftSkills/soft_skills.csv"
        )