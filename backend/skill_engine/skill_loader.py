import pandas as pd


class SkillLoader:

    def __init__(self):

        self.skills = self.load_skills()

    def load_skills(self):

        df = pd.read_csv(
            "Data/KnowledgeBase/Skills/skills.csv"
        )

        return set(
            df["skill_name"]
            .dropna()
            .astype(str)
        )