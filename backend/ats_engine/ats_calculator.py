class ATSCalculator:

    def __init__(self):

        pass


    def calculate(

        self,

        candidate_profile,

        skill_gap_result

    ):

        matched = len(

            skill_gap_result["matched_skills"]

        )

        missing = len(

            skill_gap_result["missing_skills"]

        )

        total = matched + missing

        if total == 0:

            skill_score = 0

        else:

            skill_score = (

                matched / total

            ) * 100

        education_score = 0

        if candidate_profile["education"]["normalized_degrees"]:

            education_score = 20

        project_score = min(

            len(

                candidate_profile["projects"]["projects"]

            ) * 5,

            20

        )

        certification_score = min(

            len(

                candidate_profile["certifications"]["certifications"]

            ) * 5,

            20

        )

        final_score = (

            skill_score * 0.4 +

            education_score +

            project_score +

            certification_score

        )

        if final_score > 100:

            final_score = 100

        return round(final_score, 2)