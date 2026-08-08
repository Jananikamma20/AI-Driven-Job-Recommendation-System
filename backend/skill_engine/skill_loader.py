import pandas as pd


class SkillLoader:

    def __init__(self):

        self.skills = self.load_skills()

    def load_skills(self):

        df = pd.read_csv(
            "Data/KnowledgeBase/Skills/skills.csv"
        )

        skills = set()

        # -----------------------------------------
        # Main skill name
        # -----------------------------------------

        if "skill_name" in df.columns:

            skills.update(
                df["skill_name"]
                .dropna()
                .astype(str)
                .str.strip()
            )

        # -----------------------------------------
        # Actual skill / normalized skill column
        # -----------------------------------------

        if "skill" in df.columns:

            skills.update(
                df["skill"]
                .dropna()
                .astype(str)
                .str.strip()
            )

        # -----------------------------------------
        # Abbreviations / aliases
        # -----------------------------------------

        if "abbreviation" in df.columns:

            skills.update(
                df["abbreviation"]
                .dropna()
                .astype(str)
                .str.strip()
            )

        return skills