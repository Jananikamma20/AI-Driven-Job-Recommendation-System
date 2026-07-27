import re

from backend.skill_engine.skill_loader import SkillLoader


class SkillDetector:

    def __init__(self):

        self.loader = SkillLoader()

        self.skills = self.loader.load(
            "backend/knowledgebase/skills.csv"
        )


    def detect(self, resume_text):

        detected_skills = []

        resume_text = resume_text.lower()

        for skill in self.skills:
            if len(skill) <= 1:
                continue
        
            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, resume_text, re.IGNORECASE):

                detected_skills.append(skill)

        return sorted(list(set(detected_skills)))