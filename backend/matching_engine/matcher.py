class ResumeJobMatcher:

    def __init__(self):
        pass

    def match_skills(self, resume_skills, job_skills):

        resume_skills = set(resume_skills)

        job_skills = set(job_skills)

        matched_skills = list(
            resume_skills.intersection(job_skills)
        )

        missing_skills = list(
            job_skills - resume_skills
        )

        if len(job_skills) == 0:

            score = 0

        else:

            score = (
                len(matched_skills)
                /
                len(job_skills)
            ) * 100

        return {

            "matched_skills": sorted(matched_skills),

            "missing_skills": sorted(missing_skills),

            "skill_score": round(score, 2)

        }

    def match_degree(self, resume_degrees, job_degrees):

        resume_degrees = set(resume_degrees)

        job_degrees = set(job_degrees)

        matched = list(
            resume_degrees.intersection(job_degrees)
        )

        return {

            "degree_match": len(matched) > 0,

            "matched_degrees": sorted(matched)

        }

    def match_experience(self, resume_exp, job_exp):

        resume_exp = set(resume_exp)

        job_exp = set(job_exp)

        matched = list(
            resume_exp.intersection(job_exp)
        )

        return {

            "experience_match": len(matched) > 0,

            "matched_experience": sorted(matched)

        }

    def match_certifications(

            self,

            resume_certifications,

            job_certifications

    ):

        resume_certifications = set(

            resume_certifications

        )

        job_certifications = set(

            job_certifications

        )

        matched = list(

            resume_certifications.intersection(

                job_certifications

            )

        )

        return {

            "certification_match":

            len(matched) > 0,

            "matched_certifications":

            sorted(matched)

        }

    def calculate_final_score(

            self,

            skill_score,

            degree_match,

            experience_match,

            certification_match

    ):

        score = skill_score * 0.70

        if degree_match:

            score += 15

        if experience_match:

            score += 10

        if certification_match:

            score += 5

        return round(score,2)

    def match(

            self,

            resume,

            job

    ):
        skill_result = self.match_skills(

            resume.get("skills", []),

            job.get("skills", [])

        )

        degree_result = self.match_degree(

            resume.get("degrees", []),

            job.get("degrees", [])

        )

        experience_result = self.match_experience(

            resume.get("experience", []),

            job.get("experience", [])

        )

        certification_result = self.match_certifications(

            resume.get("certifications", []),

            job.get("certifications", [])

        )

        final_score = self.calculate_final_score(

            skill_result["skill_score"],

            degree_result["degree_match"],

            experience_result["experience_match"],

            certification_result["certification_match"]

        )

        return {

            "match_score": final_score,

            "matched_skills": skill_result["matched_skills"],

            "missing_skills": skill_result["missing_skills"],

            "degree_match": degree_result["degree_match"],

            "experience_match": experience_result["experience_match"],

            "certification_match": certification_result["certification_match"]

        }