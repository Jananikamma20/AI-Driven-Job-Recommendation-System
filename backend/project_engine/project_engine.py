class ProjectEngine:

    def __init__(self):

        pass

    # ---------------------------------
    # Match Resume Projects with Job
    # ---------------------------------
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

        matched_projects = []

        missing_projects = []

        job_text = job_text.lower()

        for project in resume_projects:

            if project.lower() in job_text:

                matched_projects.append(

                    project

                )

            else:

                missing_projects.append(

                    project

                )

        score = (

            len(matched_projects)

            /

            len(resume_projects)

        ) * 100

        return {

            "matched_projects":

            sorted(matched_projects),

            "missing_projects":

            sorted(missing_projects),

            "project_score":

            round(score, 2)

        }