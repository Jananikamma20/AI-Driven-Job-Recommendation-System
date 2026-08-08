from backend.matching_engine.matcher import (
    ResumeJobMatcher
)


class ATSEngine:

    def __init__(self):

        self.matcher = ResumeJobMatcher()

    # =====================================================
    # CALCULATE ATS SCORE
    # =====================================================

    def calculate_ats_score(
        self,
        resume,
        job
    ):

        result = self.matcher.match(
            resume,
            job
        )

        # ---------------------------------------------
        # ATS weights
        #
        # Skills        = 50%
        # Education     = 15%
        # Experience    = 15%
        # Certification = 10%
        # Projects      = 10%
        # ---------------------------------------------

        ats_score = (

            result["skill_score"] * 0.50

            +

            result["degree_score"] * 0.15

            +

            result["experience_score"] * 0.15

            +

            result["certification_score"] * 0.10

            +

            result["project_score"] * 0.10

        )

        ats_score = round(
            ats_score,
            2
        )

        # ---------------------------------------------
        # Missing keywords
        # ---------------------------------------------

        missing_keywords = (
            result[
                "missing_skills"
            ]
        )

        # ---------------------------------------------
        # Suggestions
        # ---------------------------------------------

        suggestions = []

        for skill in missing_keywords:

            suggestions.append(

                "Add "
                +
                skill
                +
                " to your resume"

            )

        # ---------------------------------------------
        # ATS Rating
        # ---------------------------------------------

        if ats_score >= 90:

            rating = "Excellent"

        elif ats_score >= 75:

            rating = "Good"

        elif ats_score >= 60:

            rating = "Average"

        else:

            rating = "Needs Improvement"

        return {

            "ats_score":
                ats_score,

            "rating":
                rating,

            "missing_keywords":
                missing_keywords,

            "suggestions":
                suggestions,

            "skill_score":
                result[
                    "skill_score"
                ],

            "education_score":
                result[
                    "degree_score"
                ],

            "experience_score":
                result[
                    "experience_score"
                ],

            "certification_score":
                result[
                    "certification_score"
                ],

            "project_score":
                result[
                    "project_score"
                ]

        }