from datetime import datetime

from backend.skill_engine.skill_engine import SkillEngine
from backend.matching_engine.matcher import ResumeJobMatcher
from backend.skill_gap_engine.skill_gap_engine import SkillGapEngine
from backend.course_engine.course_engine import CourseEngine
from backend.ats_engine.ats_engine import ATSEngine
from backend.project_engine.project_engine import ProjectEngine
from backend.experience_engine.experience_engine import ExperienceEngine
from backend.education_engine.education_engine import EducationEngine
from backend.certification_engine.certification_engine import CertificationEngine


class RecommendationEngine:

    def __init__(self):

        self.skill_engine = SkillEngine()

        self.matcher = ResumeJobMatcher()

        self.skill_gap_engine = SkillGapEngine()

        self.course_engine = CourseEngine()

        self.ats_engine = ATSEngine()

        self.project_engine = ProjectEngine()

        self.experience_engine = ExperienceEngine()

        self.education_engine = EducationEngine()

        self.certification_engine = CertificationEngine()

    # =====================================================
    # NORMALIZE RESUME DATA
    # =====================================================

    def _normalize_resume(self, resume):

        normalized = {}

        # -------------------------------------------------
        # Skills
        # -------------------------------------------------

        skills = resume.get("skills", [])

        if isinstance(skills, dict):

            skills = (
                skills.get("normalized_skills")
                or skills.get("skills")
                or []
            )

        normalized["skills"] = skills or []

        # -------------------------------------------------
        # Education / Degrees
        # -------------------------------------------------

        education = resume.get("education", {})

        if isinstance(education, dict):

            degrees = (
                education.get("normalized_degrees")
                or education.get("degrees")
                or []
            )

        else:

            degrees = education or []

        normalized["degrees"] = degrees

        # -------------------------------------------------
        # Experience
        # -------------------------------------------------

        experience = resume.get(
            "experience",
            []
        )

        if isinstance(experience, dict):

            experience_list = (
                experience.get("experience")
                or experience.get("experiences")
                or experience.get("years")
                or []
            )

            # If the engine returned a dictionary but did
            # not provide a list, use the original values
            # that may contain useful experience text.
            if not experience_list:

                experience_list = []

        else:

            experience_list = experience

        normalized["experience"] = (
            experience_list or []
        )

        # -------------------------------------------------
        # Certifications
        # -------------------------------------------------

        certifications = resume.get(
            "certifications",
            []
        )

        if isinstance(certifications, dict):

            certifications = (
                certifications.get(
                    "normalized_certifications"
                )
                or certifications.get(
                    "certifications"
                )
                or []
            )

        normalized["certifications"] = (
            certifications or []
        )

        # -------------------------------------------------
        # Projects
        # -------------------------------------------------

        projects = resume.get(
            "projects",
            []
        )

        if isinstance(projects, dict):

            projects = (
                projects.get("projects")
                or []
            )

        normalized["projects"] = (
            projects or []
        )

        # -------------------------------------------------
        # Preserve cleaned text
        # -------------------------------------------------

        normalized["cleaned_text"] = resume.get(
            "cleaned_text",
            ""
        )

        return normalized

    # =====================================================
    # COMPLETE RESUME ANALYSIS
    # =====================================================

    def analyze(

        self,

        resume,

        job

    ):

        # -------------------------------------------------
        # Validate input
        # -------------------------------------------------

        if not resume:

            return {

                "status": "error",

                "message":
                "Resume data is empty."

            }

        if not job:

            return {

                "status": "error",

                "message":
                "Job data is empty."

            }

        # -------------------------------------------------
        # Convert frontend resume profile into the
        # flat structure expected by the engines
        # -------------------------------------------------

        resume = self._normalize_resume(
            resume
        )

        # -------------------------------------------------
        # Validate normalized resume
        # -------------------------------------------------

        required_resume_fields = [

            "skills",

            "degrees",

            "experience",

            "certifications"

        ]

        for field in required_resume_fields:

            if field not in resume:

                return {

                    "status": "error",

                    "message":
                    f"Resume is missing '{field}'."

                }

        # -------------------------------------------------
        # Validate job
        # -------------------------------------------------

        required_job_fields = [

            "skills",

            "degrees",

            "experience",

            "certifications"

        ]

        for field in required_job_fields:

            if field not in job:

                return {

                    "status": "error",

                    "message":
                    f"Job is missing '{field}'."

                }

        # -------------------------------------------------
        # Timestamp
        # -------------------------------------------------

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # =================================================
        # SKILL ANALYSIS
        # =================================================

        skill_analysis = self.skill_engine.analyze(

            resume,

            job

        )

        # =================================================
        # RESUME-JOB MATCHING
        # =================================================

        matching = self.matcher.match(

            resume,

            job

        )

        # =================================================
        # SKILL GAP
        # =================================================

        skill_gap = (
            self.skill_gap_engine.analyze_skill_gap(
                matching
            )
        )

        # =================================================
        # COURSE RECOMMENDATION
        # =================================================

        recommended_courses = (
            self.course_engine.recommend_courses(
                skill_gap["missing_skills"]
            )
        )

        # =================================================
        # ATS ANALYSIS
        # =================================================

        ats = self.ats_engine.calculate_ats_score(

            resume,

            job

        )

        # =================================================
        # EXPERIENCE ANALYSIS
        # =================================================

        experience = self.experience_engine.analyze(

            resume,

            job

        )

        # =================================================
        # EDUCATION ANALYSIS
        # =================================================

        education = self.education_engine.analyze(

            resume,

            job

        )

        # =================================================
        # CERTIFICATION ANALYSIS
        # =================================================

        certification = (
            self.certification_engine.analyze(

                resume,

                job

            )
        )

        # =================================================
        # PROJECT ANALYSIS
        # =================================================

        projects = self.project_engine.match_projects(

            resume.get(
                "projects",
                []
            ),

            job.get(
                "description",
                ""
            )

        )

        # =================================================
        # SUMMARY
        # =================================================

        summary = {

            "overall_match":
                matching["match_score"],

            "ats_score":
                ats["ats_score"],

            "recommendation":

                "Excellent Match"

                if matching["match_score"] >= 90

                else

                "Highly Recommended"

                if matching["match_score"] >= 75

                else

                "Recommended"

                if matching["match_score"] >= 60

                else

                "Needs Improvement"

        }

        # =================================================
        # STATISTICS
        # =================================================

        statistics = {

            "total_resume_skills":
                len(
                    resume.get(
                        "skills",
                        []
                    )
                ),

            "total_job_skills":
                len(
                    job.get(
                        "skills",
                        []
                    )
                ),

            "matched_skills":
                len(
                    matching[
                        "matched_skills"
                    ]
                ),

            "missing_skills":
                len(
                    matching[
                        "missing_skills"
                    ]
                ),

            "recommended_courses":
                len(
                    recommended_courses
                )

        }

        # =================================================
        # FINAL RESULT
        # =================================================

        return {

            "status":
                "success",

            "message":
                "Recommendation generated successfully.",

            "generated_at":
                timestamp,

            "summary":
                summary,

            "statistics":
                statistics,

            "data": {

                "skill_analysis":
                    skill_analysis,

                "matching":
                    matching,

                "skill_gap":
                    skill_gap,

                "recommended_courses":
                    recommended_courses,

                "ats":
                    ats,

                "experience":
                    experience,

                "education":
                    education,

                "certification":
                    certification,

                "projects":
                    projects

            }

        }