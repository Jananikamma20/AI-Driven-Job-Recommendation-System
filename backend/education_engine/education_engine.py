class EducationEngine:

    def __init__(self):

        pass

    # ---------------------------------
    # Compare Resume and Job Degrees
    # ---------------------------------
    def compare_education(

            self,

            resume_degrees,

            job_degrees

    ):

        if not resume_degrees:

            return {

                "education_match": False,

                "matched_degrees": [],

                "missing_degrees": job_degrees,

                "education_score": 0

            }

        if not job_degrees:

            return {

                "education_match": True,

                "matched_degrees": [],

                "missing_degrees": [],

                "education_score": 100

            }

        resume_set = {

            degree.lower()

            for degree in resume_degrees

        }

        job_set = {

            degree.lower()

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

            round(score, 2)

        }

    # ---------------------------------
    # Complete Education Analysis
    # ---------------------------------
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