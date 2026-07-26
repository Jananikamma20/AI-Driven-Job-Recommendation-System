from backend.skill_engine.skill_detector import SkillDetector
from backend.skill_engine.skill_normalizer import SkillNormalizer


class SkillEngine:

    def __init__(self):

        self.detector = SkillDetector()

        self.normalizer = SkillNormalizer()


    def extract(self, resume_text):

        detected_skills = self.detector.detect(
            resume_text
        )

        normalized_skills = self.normalizer.normalize(
            detected_skills
        )

        return {

            "detected_skills": detected_skills,

            "normalized_skills": normalized_skills

        }