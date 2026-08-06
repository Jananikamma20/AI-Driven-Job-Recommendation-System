class SkillGapEngine:

    def __init__(self):
        pass

    def analyze_skill_gap(self, matching_result):

        missing_skills = matching_result.get(

            "missing_skills",

            []

        )

        priority = {}

        for skill in missing_skills:

            priority[skill] = "High"

        recommendations = []

        for skill in missing_skills:

            recommendations.append(

                "Learn " + skill

            )

        matched_skills = matching_result.get(

            "matched_skills",

            []

        )
        total_skills = len(matched_skills) + len(missing_skills)

        if total_skills == 0:

            gap_percentage = 0

        else:

            gap_percentage = (

                len(missing_skills)

                /

                total_skills

            ) * 100

        return {

            "gap_percentage": round(gap_percentage, 2),

            "missing_skills": missing_skills,

            "priority": priority,

            "recommendations": recommendations

        }