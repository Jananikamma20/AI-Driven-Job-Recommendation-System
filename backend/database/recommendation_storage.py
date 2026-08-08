from backend.database.operations import (
    insert_resume,
    insert_job,
    insert_recommendation
)


class RecommendationStorage:

    def save_analysis(

        self,

        user_id,

        resume,

        job,

        recommendation_result,

        resume_file_name=""

    ):

        resume_id = insert_resume(

            user_id,

            resume_file_name,

            resume

        )

        job_id = insert_job(

            job.get("title", ""),

            job.get("company", ""),

            job

        )

        recommendation_id = insert_recommendation(

            resume_id,

            job_id,

            recommendation_result

        )

        return {

            "resume_id": resume_id,

            "job_id": job_id,

            "recommendation_id": recommendation_id

        }