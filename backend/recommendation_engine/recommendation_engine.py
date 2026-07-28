from backend.recommendation_engine.recommendation_validator import RecommendationValidator


class RecommendationEngine:

    def __init__(self):

        self.validator = RecommendationValidator()


    def recommend(

        self,

        candidate_profile,

        jobs,

        top_k=5

    ):

        candidate_skills = []

        if "normalized_skills" in candidate_profile["skills"]:

            candidate_skills = [

                skill.lower()

                for skill in

                candidate_profile["skills"]["normalized_skills"]

            ]

        recommendations = []

        for _, job in jobs.iterrows():

            score = 0

            text = str(job).lower()

            for skill in candidate_skills:

                if skill in text:

                    score += 1

            recommendations.append(

                {

                    "score": score,

                    "job": job.to_dict()

                }

            )

        recommendations = sorted(

            recommendations,

            key=lambda x: x["score"],

            reverse=True

        )

        valid, invalid = self.validator.validate(

            recommendations

        )

        return {

            "recommended_jobs": valid[:top_k],

            "rejected_jobs": invalid

        }