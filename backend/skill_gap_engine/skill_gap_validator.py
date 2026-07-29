class SkillGapValidator:

    def __init__(self):

        pass


    def validate(self, result):

        matched = list(

            dict.fromkeys(

                result["matched_skills"]

            )

        )

        missing = list(

            dict.fromkeys(

                result["missing_skills"]

            )

        )

        return {

            "matched_skills": matched,

            "missing_skills": missing

        }