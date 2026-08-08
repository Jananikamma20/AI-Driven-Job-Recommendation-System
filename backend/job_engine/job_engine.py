import re

from backend.job_engine.job_loader import JobLoader
from backend.job_engine.job_validator import JobValidator

from backend.skill_engine.skill_engine import SkillEngine
from backend.education_engine.education_engine import EducationEngine
from backend.certification_engine.certification_engine import CertificationEngine


class JobEngine:

    def __init__(self):

        self.loader = JobLoader()

        self.validator = JobValidator()

        self.skill_engine = SkillEngine()

        self.education_engine = EducationEngine()

        self.certification_engine = CertificationEngine()

    # =====================================================
    # LOAD JOBS FROM CSV
    # =====================================================

    def load_jobs(self, csv_path):

        jobs = self.loader.load(csv_path)

        jobs = self.validator.validate(jobs)

        return jobs

    # =====================================================
    # EXTRACT JOB PROFILE FROM JOB DESCRIPTION
    # =====================================================

    def extract_job_profile(self, job_description):

        if not job_description:

            return {
                "description": "",
                "skills": [],
                "degrees": [],
                "experience": [],
                "certifications": []
            }

        job_description = str(
            job_description
        ).strip()

        # -------------------------------------------------
        # Extract skills
        # -------------------------------------------------

        skill_result = self.skill_engine.extract(
            job_description
        )

        if isinstance(skill_result, dict):

            skills = (
                skill_result.get("normalized_skills")
                or skill_result.get("skills")
                or skill_result.get("detected_skills")
                or []
            )

        else:

            skills = skill_result or []

        # -------------------------------------------------
        # Extract education
        # -------------------------------------------------

        education_result = self.education_engine.extract(
            job_description
        )

        degrees = education_result.get(
            "normalized_degrees",
            []
        )

        # -------------------------------------------------
        # Extract certifications
        # -------------------------------------------------

        certification_result = (
            self.certification_engine.extract(
                job_description
            )
        )

        certifications = (
            certification_result.get(
                "certifications",
                []
            )
        )

        # -------------------------------------------------
        # Extract experience requirements
        # -------------------------------------------------

        experience = self._extract_experience(
            job_description
        )

        # -------------------------------------------------
        # Return structured job profile
        # -------------------------------------------------

        return {

            "description":
                job_description,

            "skills":
                skills,

            "degrees":
                degrees,

            "experience":
                experience,

            "certifications":
                certifications

        }

    # =====================================================
    # EXTRACT EXPERIENCE REQUIREMENT
    # =====================================================

    def _extract_experience(self, text):

        if not text:

            return []

        patterns = [

            r"\d+\+?\s*(?:years?|yrs?)\s+of\s+experience",

            r"\d+\+?\s*(?:years?|yrs?)\s+experience",

            r"experience\s*[:\-]?\s*\d+\+?\s*(?:years?|yrs?)"

        ]

        results = []

        for pattern in patterns:

            matches = re.findall(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            results.extend(
                matches
            )

        return sorted(
            list(
                set(
                    results
                )
            )
        )