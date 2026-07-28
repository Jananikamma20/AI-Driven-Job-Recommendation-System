from backend.job_engine.job_loader import JobLoader

loader = JobLoader()

jobs = loader.load(

    "Data/Jobs/jobs_10000.csv"

)

print(jobs.head())

print()

print(jobs.columns)

print()

print("Total Jobs:", len(jobs))