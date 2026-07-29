from backend.skill_gap_engine.skill_gap_analyzer import SkillGapAnalyzer

from backend.skill_gap_engine.skill_gap_validator import SkillGapValidator


class SkillGapEngine:

    def __init__(self):

        self.analyzer = SkillGapAnalyzer()

        self.validator = SkillGapValidator()


    def analyze(

        self,

        candidate_profile,

        job_description

    ):

        result = self.analyzer.analyze(

            candidate_profile,

            job_description

        )

        return self.validator.validate(

            result

        )