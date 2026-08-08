import re


class ProjectEngine:

    def __init__(self):
        pass

    # =====================================================
    # EXTRACT PROJECTS
    # =====================================================

    def extract(self, text):

        if not text:
            return {
                "projects": []
            }

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        projects = []

        project_section = False

        section_headers = [
            "projects",
            "project",
            "academic projects",
            "personal projects",
            "key projects"
        ]

        ending_sections = [
            "education",
            "experience",
            "work experience",
            "skills",
            "certifications",
            "achievements",
            "languages",
            "interests",
            "references"
        ]

        description_keywords = [
            "built ",
            "developed ",
            "created ",
            "designed ",
            "implemented ",
            "performed ",
            "generated ",
            "used ",
            "worked ",
            "responsible for",
            "developing ",
            "using "
        ]

        for line in lines:

            lower_line = line.lower().strip()

            if lower_line in section_headers:

                project_section = True
                continue

            if lower_line in ending_sections:

                project_section = False
                continue

            if not project_section:
                continue

            if "tech stack" in lower_line:
                continue

            if any(
                lower_line.startswith(keyword)
                for keyword in description_keywords
            ):
                continue

            if len(line.split()) > 15:
                continue

            projects.append(line)

        projects = sorted(
            list(set(projects))
        )

        return {
            "projects": projects
        }

    # =====================================================
    # PROJECT KEYWORD EXTRACTION
    # =====================================================

    def _get_keywords(self, text):

        text = str(text).lower()

        keyword_patterns = {

            "python": [
                "python"
            ],

            "pandas": [
                "pandas"
            ],

            "scikit-learn": [
                "scikit-learn",
                "sklearn"
            ],

            "machine learning": [
                "machine learning",
                "ml"
            ],

            "k-means": [
                "k-means",
                "kmeans",
                "clustering"
            ],

            "nlp": [
                "nlp",
                "natural language processing"
            ],

            "sql": [
                "sql",
                "mysql"
            ],

            "flask": [
                "flask"
            ],

            "tableau": [
                "tableau"
            ],

            "power bi": [
                "power bi"
            ],

            "streamlit": [
                "streamlit"
            ],

            "plotly": [
                "plotly"
            ],

            "yfinance": [
                "yfinance"
            ],

            "data analysis": [
                "data analysis",
                "data analytics",
                "data science"
            ],

            "data visualization": [
                "data visualization",
                "visualization",
                "dashboard",
                "dashboards"
            ],

            "stock analysis": [
                "stock analysis",
                "stock market",
                "financial analysis"
            ],

            "feature scaling": [
                "feature scaling",
                "data preprocessing",
                "preprocessing"
            ],

            "resume parsing": [
                "resume parsing",
                "resume parser"
            ],

            "skill gap": [
                "skill gap",
                "skill-gap"
            ]

        }

        found = set()

        for normalized_keyword, patterns in keyword_patterns.items():

            for pattern in patterns:

                if re.search(
                    r"\b" +
                    re.escape(pattern) +
                    r"\b",
                    text
                ):

                    found.add(
                        normalized_keyword
                    )

                    break

        return found

    # =====================================================
    # PROJECT MATCHING
    # =====================================================

    def match_projects(

        self,

        resume_projects,

        job_text

    ):

        if not resume_projects:

            return {
                "matched_projects": [],
                "missing_projects": [],
                "project_score": 0
            }

        if not job_text:

            return {
                "matched_projects": [],
                "missing_projects": resume_projects,
                "project_score": 0
            }

        job_text = str(
            job_text
        ).lower()

        job_keywords = self._get_keywords(
            job_text
        )

        matched_projects = []
        missing_projects = []

        for project in resume_projects:

            project_keywords = self._get_keywords(
                project
            )

            if not project_keywords:

                missing_projects.append(
                    project
                )

                continue

            matched_keywords = (
                project_keywords
                &
                job_keywords
            )

            # -----------------------------------------
            # Project relevance
            # -----------------------------------------

            project_match_score = (

                len(matched_keywords)

                /

                len(project_keywords)

            ) * 100

            # -----------------------------------------
            # A project is relevant when at least
            # one meaningful technology/domain keyword
            # matches the job.
            # -----------------------------------------

            if (
                len(matched_keywords) >= 1
                and
                project_match_score >= 20
            ):

                matched_projects.append(
                    project
                )

            else:

                missing_projects.append(
                    project
                )

        # =================================================
        # FINAL PROJECT SCORE
        # =================================================

        project_score = (

            len(matched_projects)

            /

            len(resume_projects)

        ) * 100

        return {

            "matched_projects":
                sorted(
                    matched_projects
                ),

            "missing_projects":
                sorted(
                    missing_projects
                ),

            "project_score":
                round(
                    project_score,
                    2
                )

        }