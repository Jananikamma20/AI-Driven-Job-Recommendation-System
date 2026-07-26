class SkillMatcher:

    def __init__(self):

        pass


    def match(

            self,

            candidate_skills,

            job_skills

    ):

        candidate = set(

            skill.lower()

            for skill in candidate_skills

        )

        job = set(

            skill.lower()

            for skill in job_skills

        )

        matched = sorted(

            list(

                candidate.intersection(job)

            )

        )

        missing = sorted(

            list(

                job.difference(candidate)

            )

        )

        if len(job) == 0:

            percentage = 0

        else:

            percentage = round(

                (

                    len(matched)

                    /

                    len(job)

                ) * 100,

                2

            )

        return {

            "matched_skills": matched,

            "missing_skills": missing,

            "match_percentage": percentage

        }