class SkillMatcher:

    def __init__(self):

        pass

    def match(

            self,

            resume_skills,

            job_skills

    ):

        resume = set(resume_skills)

        job = set(job_skills)

        matched = list(
            resume.intersection(job)
        )

        missing = list(
            job - resume
        )

        score = 0

        if len(job) > 0:

            score = (
                len(matched)
                /
                len(job)
            ) * 100

        return {

            "matched_skills":
                sorted(matched),

            "missing_skills":
                sorted(missing),

            "skill_score":
                round(score, 2)

        }