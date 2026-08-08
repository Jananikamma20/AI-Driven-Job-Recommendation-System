print("recommendation_routes.py loaded")


from flask import Blueprint
from flask import request
from flask import jsonify


from backend.pipeline.resume_pipeline import (
    ResumePipeline
)

from backend.job_engine.job_engine import (
    JobEngine
)

from backend.recommendation_engine.recommendation_engine import (
    RecommendationEngine
)

from backend.Services.recommendation_service import (
    RecommendationService
)

from backend.database.operations import (
    get_user
)


# =========================================================
# BLUEPRINT
# =========================================================

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)


# =========================================================
# EXISTING COMPONENTS
# =========================================================

resume_pipeline = ResumePipeline()

job_engine = JobEngine()

recommendation_engine = RecommendationEngine()

recommendation_service = RecommendationService()


# =========================================================
# EXISTING JOB RECOMMENDATION ROUTE
# =========================================================


@recommendation_bp.route(
    "/recommend-jobs",
    methods=["POST"]
)
def recommend_jobs():

    print("Step 1")

    # -----------------------------------------
    # Validate resume
    # -----------------------------------------

    if "resume" not in request.files:

        return jsonify({

            "error":
            "Resume file not found."

        }), 400


    file = request.files["resume"]


    print("Step 2")


    # -----------------------------------------
    # Save temporary resume
    # -----------------------------------------

    save_path = "temp_resume.pdf"

    file.save(save_path)


    print("Step 3")


    # -----------------------------------------
    # Parse resume
    # -----------------------------------------

    candidate = resume_pipeline.process_resume(
        save_path
    )


    print("Step 4")


    # -----------------------------------------
    # Load jobs
    # -----------------------------------------

    jobs = job_engine.load_jobs(
        "Data/Jobs/jobs_10000.csv"
    )


    print("Step 5")


    # -----------------------------------------
    # Recommend top jobs
    # -----------------------------------------

    recommendations = recommendation_engine.recommend(

        candidate[
            "candidate_profile"
        ][
            "candidate_profile"
        ],

        jobs,

        top_k=5

    )


    print("Step 6")


    return jsonify({

        "recommendations":
        recommendations

    })


@recommendation_bp.route(
    "/analyze-recommendation",
    methods=["POST"]
)
def analyze_recommendation():

    print(
        "V2 Recommendation Analysis Started"
    )


    # -----------------------------------------
    # Get JSON request
    # -----------------------------------------

    data = request.get_json()


    if not data:

        return jsonify({

            "status": "error",

            "message":
            "Request data is empty."

        }), 400


    # -----------------------------------------
    # Get resume
    # -----------------------------------------

    resume = data.get(
        "resume"
    )


    if not resume:

        return jsonify({

            "status": "error",

            "message":
            "Resume data is missing."

        }), 400


    # -----------------------------------------
    # Get job
    # -----------------------------------------

    job_data = data.get(
        "job"
    )

    if not job_data:

        return jsonify({

            "status": "error",

            "message":
            "Job data is missing."

        }), 400
    # -----------------------------------------
    # Extract structured job profile
    # -----------------------------------------

    if isinstance(job_data, dict):

        job_description = job_data.get(
            "description",
            ""
        )

    else:

        job_description = str(
            job_data
        )

    if not job_description.strip():

        return jsonify({

            "status": "error",

            "message":
            "Job description is empty."

        }), 400


    job = job_engine.extract_job_profile(
        job_description
    )

    # -----------------------------------------
    # Get user ID
    # -----------------------------------------
    #
    # Authentication is not part of V2 yet.
    # Therefore user_id defaults to 1.
    #
    # -----------------------------------------

    user_id = data.get(
        "user_id",
        1
    )


    # -----------------------------------------
    # Verify user
    # -----------------------------------------

    if not get_user(user_id):

        return jsonify({

            "status": "error",

            "message":
            "User not found."

        }), 400


    # -----------------------------------------
    # Resume file name
    # -----------------------------------------

    resume_file_name = data.get(

        "resume_file_name",

        ""

    )


    # -----------------------------------------
    # Run Recommendation Service
    # -----------------------------------------

    result = recommendation_service.analyze_and_save(

        user_id,

        resume,

        job,

        resume_file_name

    )


    # -----------------------------------------
    # Return result
    # -----------------------------------------

    return jsonify(
        result
    )

@recommendation_bp.route(
    "/recommendation-history",
    methods=["GET"]
)
def recommendation_history():

    print(
        "Recommendation History Requested"
    )


    history = recommendation_service.get_history()


    return jsonify({

        "status": "success",

        "count": len(history),

        "history": history

    })