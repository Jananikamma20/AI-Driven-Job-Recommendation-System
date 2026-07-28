from backend.job_engine.job_loader import JobLoader
from backend.job_engine.job_validator import JobValidator


class JobEngine:

    def __init__(self):

        self.loader = JobLoader()

        self.validator = JobValidator()


    def load_jobs(self, csv_path):

        jobs = self.loader.load(csv_path)

        jobs = self.validator.validate(jobs)

        return jobs