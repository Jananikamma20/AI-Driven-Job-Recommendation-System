from backend.job_engine.job_engine import JobEngine

engine = JobEngine()

jobs = engine.load_jobs(

    "Data/Jobs/jobs_10000.csv"

)

print("=" * 60)
print("JOB DATASET")
print("=" * 60)

print(jobs.head())

print()

print("Total Jobs :", len(jobs))

print()

print(jobs.columns)

print()

print(jobs.info())

print()

print(jobs.describe(include="all"))