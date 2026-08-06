from backend.skill_engine.skill_loader import SkillLoader
from backend.skill_engine.skill_detector import SkillDetector
from backend.skill_engine.skill_normalizer import SkillNormalizer
from backend.skill_engine.skill_matcher import SkillMatcher


class SkillEngine:

    def __init__(self):

        self.loader = SkillLoader()

        self.detector = SkillDetector()

        self.normalizer = SkillNormalizer()

        self.matcher = SkillMatcher()

    # ---------------------------------
    # Detect Skills from Resume Text
    # ---------------------------------

    def detect_skills(self, text):

        return self.detector.detect(

            text,

            self.loader.skills

        )

    # ---------------------------------
    # Analyze Resume & Job Skills
    # ---------------------------------

    def analyze(

            self,

            resume,

            job

    ):

        resume_skills = self.normalizer.normalize(

            resume.get(

                "skills",

                []

            )

        )

        job_skills = self.normalizer.normalize(

            job.get(

                "skills",

                []

            )

        )

        result = self.matcher.match(

            resume_skills,

            job_skills

        )

        return {

            "total_resume_skills":

            len(resume_skills),

            "total_job_skills":

            len(job_skills),

            "matched_skills":

            result["matched_skills"],

            "missing_skills":

            result["missing_skills"],

            "skill_score":

            result["skill_score"]

        }