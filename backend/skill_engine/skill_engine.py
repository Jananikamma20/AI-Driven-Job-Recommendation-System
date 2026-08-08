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

    # =====================================================
    # DETECT SKILLS FROM RESUME TEXT
    # =====================================================

    def detect_skills(

        self,

        text

    ):

        return self.detector.detect(

            text,

            self.loader.skills

        )

    # =====================================================
    # EXTRACT SKILLS FROM RESUME
    # =====================================================

    def extract(

        self,

        text

    ):

        detected_skills = self.detect_skills(

            text

        )

        normalized_skills = self.normalizer.normalize(

            detected_skills

        )

        return {

            "detected_skills":
                detected_skills,

            "normalized_skills":
                normalized_skills

        }

    # =====================================================
    # ANALYZE RESUME AND JOB SKILLS
    # =====================================================

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