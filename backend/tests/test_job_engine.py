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

print()
print("=" * 60)
print("JOB DESCRIPTION EXTRACTION")
print("=" * 60)

job_description = """
Data Analyst

We are looking for a Data Analyst with 4 years
of experience.

Required Skills:
Python
SQL
Power BI
Excel
Machine Learning

B.Tech degree required.
"""

job_profile = engine.extract_job_profile(
    job_description
)

print()
print("Extracted Job Profile:")
print(job_profile)