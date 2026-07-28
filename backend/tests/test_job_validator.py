from backend.job_engine.job_loader import JobLoader

from backend.job_engine.job_validator import JobValidator


loader = JobLoader()

validator = JobValidator()


jobs = loader.load(

    "Data/Jobs/jobs_10000.csv"

)

print("Before Validation:", len(jobs))


jobs = validator.validate(

    jobs

)

print("After Validation:", len(jobs))

print()

print(jobs.head())

print()

print(jobs.info())

print()

print(jobs.isnull().sum())