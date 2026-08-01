print("resume_routes.py loaded")
from flask import Blueprint
from flask import request
from flask import jsonify
import os

from backend.pipeline.resume_pipeline import ResumePipeline

resume_bp = Blueprint(
    "resume",
    __name__
)

pipeline = ResumePipeline()

@resume_bp.route("/test", methods=["GET"])
def test():
    print("TEST ROUTE HIT")
    return jsonify({"message": "API is working"})


@resume_bp.route("/upload-resume", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({
            "error": "Resume file not found."
        }), 400

    file = request.files["resume"]

    save_path = "temp_resume.pdf"

    file.save(save_path)

    result = pipeline.process_resume(save_path)

    return jsonify(result)