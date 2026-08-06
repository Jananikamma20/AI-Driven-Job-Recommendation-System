import re


class ExperienceEngine:

    def __init__(self):

        pass

    # ---------------------------------
    # Extract Maximum Years of Experience
    # ---------------------------------
    def extract_years(

            self,

            experience_list

    ):

        if not experience_list:

            return 0

        max_years = 0

        for exp in experience_list:

            numbers = re.findall(

                r"\d+",

                exp

            )

            if numbers:

                years = max(

                    map(

                        int,

                        numbers

                    )

                )

                max_years = max(

                    max_years,

                    years

                )

        return max_years

    # ---------------------------------
    # Compare Resume and Job Experience
    # ---------------------------------
    def compare_experience(

            self,

            resume_experience,

            job_experience

    ):

        resume_years = self.extract_years(

            resume_experience

        )

        job_years = self.extract_years(

            job_experience

        )

        if resume_years >= job_years:

            experience_match = True

            experience_score = 100

        else:

            experience_match = False

            if job_years == 0:

                experience_score = 0

            else:

                experience_score = (

                    resume_years

                    /

                    job_years

                ) * 100

        return {

            "resume_years": resume_years,

            "job_years": job_years,

            "experience_match": experience_match,

            "experience_score": round(

                experience_score,

                2

            )

        }

    # ---------------------------------
    # Complete Experience Analysis
    # ---------------------------------
    def analyze(

            self,

            resume,

            job

    ):

        resume_experience = resume.get(

            "experience",

            []

        )

        job_experience = job.get(

            "experience",

            []

        )

        return self.compare_experience(

            resume_experience,

            job_experience

        )