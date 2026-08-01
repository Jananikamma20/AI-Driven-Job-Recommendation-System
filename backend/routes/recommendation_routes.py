print("recommendation_routes.py loaded")
from flask import Blueprint
from flask import request
from flask import jsonify

from backend.pipeline.resume_pipeline import ResumePipeline
from backend.job_engine.job_engine import JobEngine
from backend.recommendation_engine.recommendation_engine import RecommendationEngine

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)

resume_pipeline = ResumePipeline()
job_engine = JobEngine()
recommendation_engine = RecommendationEngine()


@recommendation_bp.route("/recommend-jobs", methods=["POST"])
def recommend_jobs():

    print("Step 1")

    if "resume" not in request.files:
        return jsonify({"error": "Resume file not found."}), 400

    file = request.files["resume"]

    print("Step 2")

    save_path = "temp_resume.pdf"
    file.save(save_path)

    print("Step 3")

    candidate = resume_pipeline.process_resume(save_path)

    print("Step 4")

    jobs = job_engine.load_jobs("Data/Jobs/jobs_10000.csv")

    print("Step 5")

    recommendations = recommendation_engine.recommend(
        candidate["candidate_profile"]["candidate_profile"],
        jobs,
        top_k=5
    )

    print("Step 6")

    return jsonify({
        "recommendations": recommendations
    })