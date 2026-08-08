from backend.recommendation_engine.recommendation_engine import (
    RecommendationEngine
)

from backend.database.recommendation_storage import (
    RecommendationStorage
)

from backend.database.operations import (
    get_recommendation_history
)


class RecommendationService:

    def __init__(self):

        self.engine = RecommendationEngine()

        self.storage = RecommendationStorage()

    def analyze_and_save(

            self,

            user_id,

            resume,

            job,

            resume_file_name=""

    ):

        # -------------------------
        # Generate Recommendation
        # -------------------------

        result = self.engine.analyze(

            resume,

            job

        )

        # -------------------------
        # Stop if analysis failed
        # -------------------------

        if result.get("status") != "success":

            return result

        # -------------------------
        # Save Analysis
        # -------------------------

        database_result = (

            self.storage.save_analysis(

                user_id,

                resume,

                job,

                result,

                resume_file_name

            )

        )

        # -------------------------
        # Add Database IDs
        # -------------------------

        result["database"] = {

            "resume_id":

                database_result["resume_id"],

            "job_id":

                database_result["job_id"],

            "recommendation_id":

                database_result["recommendation_id"]

        }

        return result

    # ==========================================
    # GET RECOMMENDATION HISTORY
    # ==========================================

    def get_history(self):

        return get_recommendation_history()