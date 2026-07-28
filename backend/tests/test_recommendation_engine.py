from backend.pipeline.resume_pipeline import ResumePipeline

from backend.job_engine.job_engine import JobEngine

from backend.recommendation_engine.recommendation_engine import RecommendationEngine


resume_pipeline = ResumePipeline()

job_engine = JobEngine()

recommendation_engine = RecommendationEngine()

candidate = resume_pipeline.process_resume(

    "Data/Resumes/resume_pdfs/resume.pdf"

)

jobs = job_engine.load_jobs(

    "Data/Jobs/jobs_10000.csv"

)

result = recommendation_engine.recommend(

    candidate["candidate_profile"]["candidate_profile"],

    jobs,

    top_k=5

)

print("\nTOP RECOMMENDED JOBS\n")

for recommendation in result["recommended_jobs"]:

    print("=" * 60)

    print("Score :", recommendation["score"])

    print(recommendation["job"])