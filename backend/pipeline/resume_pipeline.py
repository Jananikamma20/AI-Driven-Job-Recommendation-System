from backend.resume_parser.parser import ResumeParser
from backend.experience_engine.experience_engine import ExperienceEngine
from backend.skill_engine.skill_engine import SkillEngine
from backend.education_engine.education_engine import EducationEngine


class ResumePipeline:

    def __init__(self):

        self.parser = ResumeParser()

        self.experience_engine = ExperienceEngine()

        self.skill_engine = SkillEngine()

        self.education_engine = EducationEngine()


    def process_resume(self, file_path):

        cleaned_text = self.parser.parse(file_path)

        experience = self.experience_engine.extract(
            cleaned_text
        )

        skills = self.skill_engine.extract(
            cleaned_text
        )

        education = self.education_engine.extract(
            cleaned_text
        )

        return {

            "cleaned_text": cleaned_text,

            "experience": experience,

            "skills": skills,

            "education": education

        }