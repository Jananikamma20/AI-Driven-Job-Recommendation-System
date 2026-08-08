class CertificationEngine:

    def __init__(self):
        pass

    # =====================================================
    # EXTRACT CERTIFICATIONS FROM RESUME TEXT
    # =====================================================

    def extract(

        self,

        text

    ):

        if not text:

            return {

                "certifications": []

            }

        certification_keywords = [

            "ibm data science",

            "aws certified",

            "aws",

            "azure",

            "microsoft certified",

            "google cloud",

            "google certified",

            "oracle certified",

            "cisco certified",

            "ccna",

            "pmp",

            "comptia",

            "data analyst certification",

            "python certification",

            "machine learning certification"

        ]

        text_lower = text.lower()

        certifications = []

        for certification in certification_keywords:

            if certification in text_lower:

                certifications.append(

                    certification

                )

        certifications = sorted(

            list(
                set(certifications)
            )

        )

        return {

            "certifications":
                certifications

        }

    # =====================================================
    # COMPARE RESUME AND JOB CERTIFICATIONS
    # =====================================================

    def compare_certifications(

        self,

        resume_certifications,

        job_certifications

    ):

        if not resume_certifications:

            return {

                "certification_match":
                    False,

                "matched_certifications":
                    [],

                "missing_certifications":
                    job_certifications,

                "certification_score":
                    0

            }

        if not job_certifications:

            return {

                "certification_match":
                    True,

                "matched_certifications":
                    [],

                "missing_certifications":
                    [],

                "certification_score":
                    100

            }

        resume_set = {

            str(certification)
            .lower()
            .strip()

            for certification
            in resume_certifications

        }

        job_set = {

            str(certification)
            .lower()
            .strip()

            for certification
            in job_certifications

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

            "certification_match":
                len(matched) > 0,

            "matched_certifications":
                sorted(matched),

            "missing_certifications":
                sorted(missing),

            "certification_score":
                round(
                    score,
                    2
                )

        }

    # =====================================================
    # COMPLETE CERTIFICATION ANALYSIS
    # =====================================================

    def analyze(

        self,

        resume,

        job

    ):

        resume_certifications = resume.get(

            "certifications",

            []

        )

        job_certifications = job.get(

            "certifications",

            []

        )

        return self.compare_certifications(

            resume_certifications,

            job_certifications

        )