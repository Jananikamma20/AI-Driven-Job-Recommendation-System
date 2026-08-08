import re


class ExperienceEngine:

    def __init__(self):
        pass

    # =====================================================
    # EXTRACT EXPERIENCE FROM RESUME TEXT
    # =====================================================

    def extract(self, text):

        if not text:

            return {
                "years": 0,
                "companies": [],
                "experience": []
            }

        # ---------------------------------------------
        # Find years of experience
        # ---------------------------------------------

        year_patterns = re.findall(

            r"(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)",

            text,

            flags=re.IGNORECASE

        )

        years = 0

        if year_patterns:

            years = max(
                float(value)
                for value in year_patterns
            )

        # ---------------------------------------------
        # Extract possible company names
        # ---------------------------------------------

        companies = []

        lines = [

            line.strip()

            for line in text.splitlines()

            if line.strip()

        ]

        for line in lines:

            lower_line = line.lower()

            if any(

                keyword in lower_line

                for keyword in [

                    "technologies",
                    "private limited",
                    "pvt ltd",
                    "ltd",
                    "inc",
                    "corporation",
                    "company"

                ]

            ):

                companies.append(line)

        companies = sorted(
            list(set(companies))
        )

        # ---------------------------------------------
        # Experience list
        # ---------------------------------------------

        experience_entries = []

        if years > 0:

            if years.is_integer():

                experience_entries.append(
                    f"{int(years)} years"
                )

            else:

                experience_entries.append(
                    f"{years} years"
                )

        return {

            "years": int(years)
            if years.is_integer()
            else years,

            "companies": companies,

            "experience": experience_entries

        }

    # =====================================================
    # EXTRACT MAXIMUM YEARS OF EXPERIENCE
    # =====================================================

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

                str(exp)

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

    # =====================================================
    # COMPARE RESUME AND JOB EXPERIENCE
    # =====================================================

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

        # ---------------------------------------------
        # No experience requirement
        # ---------------------------------------------

        if job_years == 0:

            return {

                "resume_years":
                    resume_years,

                "job_years":
                    job_years,

                "experience_match":
                    True,

                "experience_score":
                    100

            }

        # ---------------------------------------------
        # Candidate meets requirement
        # ---------------------------------------------

        if resume_years >= job_years:

            experience_match = True

            experience_score = 100

        # ---------------------------------------------
        # Candidate does not meet requirement
        # ---------------------------------------------

        else:

            experience_match = False

            experience_score = (

                resume_years
                /
                job_years

            ) * 100

        return {

            "resume_years":
                resume_years,

            "job_years":
                job_years,

            "experience_match":
                experience_match,

            "experience_score":
                round(
                    experience_score,
                    2
                )

        }

    # =====================================================
    # COMPLETE EXPERIENCE ANALYSIS
    # =====================================================

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