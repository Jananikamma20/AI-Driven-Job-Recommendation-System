class ResumeJobMatcher:

    def __init__(self):
        pass

    # =====================================================
    # SKILL MATCHING
    # =====================================================

    def match_skills(
        self,
        resume_skills,
        job_skills
    ):

        resume_skills = {
            str(skill).strip().lower()
            for skill in resume_skills
            if str(skill).strip()
        }

        job_skills = {
            str(skill).strip().lower()
            for skill in job_skills
            if str(skill).strip()
        }

        # No skills required by job
        if not job_skills:

            return {
                "matched_skills": [],
                "missing_skills": [],
                "skill_score": 100.0
            }

        matched_skills = (
            resume_skills.intersection(
                job_skills
            )
        )

        missing_skills = (
            job_skills - resume_skills
        )

        score = (
            len(matched_skills)
            /
            len(job_skills)
        ) * 100

        return {

            "matched_skills":
                sorted(matched_skills),

            "missing_skills":
                sorted(missing_skills),

            "skill_score":
                round(score, 2)

        }

    # =====================================================
    # EDUCATION MATCHING
    # =====================================================

    def match_degree(
        self,
        resume_degrees,
        job_degrees
    ):

        resume_degrees = {
            str(degree).strip().lower()
            for degree in resume_degrees
            if str(degree).strip()
        }

        job_degrees = {
            str(degree).strip().lower()
            for degree in job_degrees
            if str(degree).strip()
        }

        # Job does not require a degree
        if not job_degrees:

            return {

                "degree_match": True,

                "degree_score": 100.0,

                "matched_degrees": []

            }

        matched = (
            resume_degrees.intersection(
                job_degrees
            )
        )

        degree_match = (
            len(matched) > 0
        )

        return {

            "degree_match":
                degree_match,

            "degree_score":
                100.0 if degree_match else 0.0,

            "matched_degrees":
                sorted(matched)

        }

    # =====================================================
    # EXPERIENCE MATCHING
    # =====================================================

    def _extract_years(
        self,
        experience
    ):

        import re

        if not experience:
            return 0

        # Experience can be a list
        if isinstance(
            experience,
            list
        ):

            text = " ".join(
                str(item)
                for item in experience
            )

        else:

            text = str(
                experience
            )

        numbers = re.findall(
            r"\d+(?:\.\d+)?",
            text
        )

        if not numbers:
            return 0

        return max(
            float(number)
            for number in numbers
        )

    def match_experience(
        self,
        resume_exp,
        job_exp
    ):

        resume_years = (
            self._extract_years(
                resume_exp
            )
        )

        job_years = (
            self._extract_years(
                job_exp
            )
        )

        # No experience requirement
        if job_years == 0:

            return {

                "experience_match":
                    True,

                "experience_score":
                    100.0,

                "resume_years":
                    resume_years,

                "job_years":
                    job_years

            }

        # Candidate has enough experience
        if resume_years >= job_years:

            return {

                "experience_match":
                    True,

                "experience_score":
                    100.0,

                "resume_years":
                    resume_years,

                "job_years":
                    job_years

            }

        # Candidate has less experience
        score = (
            resume_years
            /
            job_years
        ) * 100

        return {

            "experience_match":
                False,

            "experience_score":
                round(
                    score,
                    2
                ),

            "resume_years":
                resume_years,

            "job_years":
                job_years

        }

    # =====================================================
    # CERTIFICATION MATCHING
    # =====================================================

    def match_certifications(

        self,

        resume_certifications,

        job_certifications

    ):

        resume_certifications = {

            str(certification)
            .strip()
            .lower()

            for certification
            in resume_certifications

            if str(certification).strip()

        }

        job_certifications = {

            str(certification)
            .strip()
            .lower()

            for certification
            in job_certifications

            if str(certification).strip()

        }

        # Job requires no certification
        if not job_certifications:

            return {

                "certification_match":
                    True,

                "certification_score":
                    100.0,

                "matched_certifications":
                    []

            }

        matched = (
            resume_certifications
            .intersection(
                job_certifications
            )
        )

        score = (

            len(matched)
            /
            len(job_certifications)

        ) * 100

        return {

            "certification_match":
                len(matched) > 0,

            "certification_score":
                round(
                    score,
                    2
                ),

            "matched_certifications":
                sorted(matched)

        }

    # =====================================================
    # OVERALL MATCH SCORE
    # =====================================================

    def calculate_final_score(

        self,

        skill_score,

        degree_score,

        experience_score,

        certification_score,

        project_score

    ):

        # ---------------------------------------------
        # Overall Match Weights
        #
        # Skills        = 40%
        # Experience    = 20%
        # Education     = 15%
        # Certification = 10%
        # Projects      = 15%
        # ---------------------------------------------

        score = (

            skill_score * 0.40

            +

            experience_score * 0.20

            +

            degree_score * 0.15

            +

            certification_score * 0.10

            +

            project_score * 0.15

        )

        return round(
            score,
            2
        )

    # =====================================================
    # COMPLETE MATCH
    # =====================================================

    def match(

        self,

        resume,

        job

    ):

        # ---------------------------------------------
        # Skills
        # ---------------------------------------------

        skill_result = self.match_skills(

            resume.get(
                "skills",
                []
            ),

            job.get(
                "skills",
                []
            )

        )

        # ---------------------------------------------
        # Education
        # ---------------------------------------------

        degree_result = self.match_degree(

            resume.get(
                "degrees",
                []
            ),

            job.get(
                "degrees",
                []
            )

        )

        # ---------------------------------------------
        # Experience
        # ---------------------------------------------

        experience_result = (
            self.match_experience(

                resume.get(
                    "experience",
                    []
                ),

                job.get(
                    "experience",
                    []
                )

            )
        )

        # ---------------------------------------------
        # Certifications
        # ---------------------------------------------

        certification_result = (
            self.match_certifications(

                resume.get(
                    "certifications",
                    []
                ),

                job.get(
                    "certifications",
                    []
                )

            )
        )

        # ---------------------------------------------
        # Projects
        # ---------------------------------------------

        from backend.project_engine.project_engine import (
            ProjectEngine
        )

        project_engine = ProjectEngine()

        project_result = (
            project_engine.match_projects(

                resume.get(
                    "projects",
                    []
                ),

                job.get(
                    "description",
                    ""
                )

            )
        )

        # ---------------------------------------------
        # Overall Score
        # ---------------------------------------------

        final_score = self.calculate_final_score(

            skill_result[
                "skill_score"
            ],

            degree_result[
                "degree_score"
            ],

            experience_result[
                "experience_score"
            ],

            certification_result[
                "certification_score"
            ],

            project_result[
                "project_score"
            ]

        )

        return {

            "match_score":
                final_score,

            "matched_skills":
                skill_result[
                    "matched_skills"
                ],

            "missing_skills":
                skill_result[
                    "missing_skills"
                ],

            "skill_score":
                skill_result[
                    "skill_score"
                ],

            "degree_match":
                degree_result[
                    "degree_match"
                ],

            "degree_score":
                degree_result[
                    "degree_score"
                ],

            "experience_match":
                experience_result[
                    "experience_match"
                ],

            "experience_score":
                experience_result[
                    "experience_score"
                ],

            "resume_years":
                experience_result[
                    "resume_years"
                ],

            "job_years":
                experience_result[
                    "job_years"
                ],

            "certification_match":
                certification_result[
                    "certification_match"
                ],

            "certification_score":
                certification_result[
                    "certification_score"
                ],

            "matched_certifications":
                certification_result[
                    "matched_certifications"
                ],

            "project_score":
                project_result[
                    "project_score"
                ],

            "matched_projects":
                project_result[
                    "matched_projects"
                ],

            "missing_projects":
                project_result[
                    "missing_projects"
                ]

        }