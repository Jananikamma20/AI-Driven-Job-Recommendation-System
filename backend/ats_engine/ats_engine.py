from backend.ats_engine.ats_calculator import ATSCalculator
from backend.ats_engine.ats_validator import ATSValidator


class ATSEngine:

    def __init__(self):

        self.calculator = ATSCalculator()

        self.validator = ATSValidator()


    def calculate(

        self,

        candidate_profile,

        skill_gap_result

    ):

        score = self.calculator.calculate(

            candidate_profile,

            skill_gap_result

        )

        score = self.validator.validate(

            score

        )

        return score