import re
class EducationEngine:

    def __init__(self):
        pass

    # =====================================================
    # EXTRACT EDUCATION FROM RESUME TEXT
    # =====================================================

    def extract(self, text):

        if not text:

            return {
                "degrees": [],
                "normalized_degrees": []
            }

        degree_patterns = {

            "b.tech": [
                r"\bb\.?tech\b",
                r"\bbachelor\s+of\s+technology\b"
            ],

            "b.e": [
                r"\bb\.?e\.?\b",
                r"\bbachelor\s+of\s+engineering\b"
            ],

            "b.sc": [
                r"\bb\.?sc\.?\b",
                r"\bbachelor\s+of\s+science\b"
            ],

            "b.com": [
                r"\bb\.?com\.?\b",
                r"\bbachelor\s+of\s+commerce\b"
            ],

            "m.tech": [
                r"\bm\.?tech\b",
                r"\bmaster\s+of\s+technology\b"
            ],

            "m.e": [
                r"\bm\.e\.?\b",
                r"\bmaster\s+of\s+engineering\b"
            ],

            "m.sc": [
                r"\bm\.?sc\.?\b",
                r"\bmaster\s+of\s+science\b"
            ],

            "mba": [
                r"\bmba\b",
                r"\bmaster\s+of\s+business\s+administration\b"
            ],

            "ph.d": [
                r"\bph\.?d\b",
                r"\bdoctor\s+of\s+philosophy\b"
            ]
        }

        degrees = []

        for normalized_name, patterns in degree_patterns.items():

            for pattern in patterns:

                if re.search(
                    pattern,
                    text,
                    flags=re.IGNORECASE
                ):

                    degrees.append(
                        normalized_name
                    )

                    break

        degrees = sorted(
            list(set(degrees))
        )

        return {

            "degrees": degrees,

            "normalized_degrees": degrees

        }

    # =====================================================
    # COMPARE RESUME AND JOB DEGREES
    # =====================================================

    def compare_education(

        self,

        resume_degrees,

        job_degrees

    ):

        if not resume_degrees:

            return {

                "education_match":
                    False,

                "matched_degrees":
                    [],

                "missing_degrees":
                    job_degrees,

                "education_score":
                    0

            }

        if not job_degrees:

            return {

                "education_match":
                    True,

                "matched_degrees":
                    [],

                "missing_degrees":
                    [],

                "education_score":
                    100

            }

        resume_set = {

            str(degree).lower().strip()

            for degree in resume_degrees

        }

        job_set = {

            str(degree).lower().strip()

            for degree in job_degrees

        }

        matched = list(

            resume_set.intersection(
                job_set
            )

        )

        missing = list(

            job_set - resume_set

        )

        score = (

            len(matched)
            /
            len(job_set)

        ) * 100

        return {

            "education_match":
                len(matched) > 0,

            "matched_degrees":
                sorted(matched),

            "missing_degrees":
                sorted(missing),

            "education_score":
                round(
                    score,
                    2
                )

        }

    # =====================================================
    # COMPLETE EDUCATION ANALYSIS
    # =====================================================

    def analyze(

        self,

        resume,

        job

    ):

        resume_degrees = resume.get(

            "degrees",

            []

        )

        job_degrees = job.get(

            "degrees",

            []

        )

        return self.compare_education(

            resume_degrees,

            job_degrees

        )