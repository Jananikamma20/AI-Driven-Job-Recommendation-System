from backend.matching_engine.matcher import ResumeJobMatcher


class ATSEngine:

    def __init__(self):

        self.matcher = ResumeJobMatcher()

    # ------------------------------------
    # Calculate ATS Score
    # ------------------------------------
    def calculate_ats_score(self, resume, job):

        # Get matching result
        result = self.matcher.match(

            resume,

            job

        )

        ats_score = result["match_score"]

        missing_keywords = result["missing_skills"]

        suggestions = []

        # Generate Suggestions
        for skill in missing_keywords:

            suggestions.append(

                "Add " + skill + " to your resume"

            )

        # ATS Rating
        if ats_score >= 90:

            rating = "Excellent"

        elif ats_score >= 75:

            rating = "Good"

        elif ats_score >= 60:

            rating = "Average"

        else:

            rating = "Needs Improvement"

        return {

            "ats_score": ats_score,

            "rating": rating,

            "missing_keywords": missing_keywords,

            "suggestions": suggestions

        }