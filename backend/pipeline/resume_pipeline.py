from backend.resume_parser.parser import ResumeParser
from backend.experience_engine.experience_engine import ExperienceEngine


class ResumePipeline:

    def __init__(self):

        self.parser = ResumeParser()

        self.experience_engine = ExperienceEngine()

    def process_resume(self, file_path):

        cleaned_text = self.parser.parse(file_path)

        experience = self.experience_engine.extract(
            cleaned_text
        )

        return {

            "cleaned_text": cleaned_text,

            "experience": experience

        }