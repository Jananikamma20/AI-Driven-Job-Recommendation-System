class ExtractorManager:

    def __init__(
        self,
        skill_engine,
        experience_engine,
        education_engine,
        project_engine,
        certification_engine
    ):

        self.skill_engine = skill_engine

        self.experience_engine = experience_engine

        self.education_engine = education_engine

        self.project_engine = project_engine

        self.certification_engine = certification_engine

    def extract_all(self, resume_text):

        return {

            "skills":
                self.skill_engine.extract(
                    resume_text
                ),

            "experience":
                self.experience_engine.extract(
                    resume_text
                ),

            "education":
                self.education_engine.extract(
                    resume_text
                ),

            "projects":
                self.project_engine.extract(
                    resume_text
                ),

            "certifications":
                self.certification_engine.extract(
                    resume_text
                )

        }