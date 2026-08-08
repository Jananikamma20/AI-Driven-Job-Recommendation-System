from backend.resume_parser.parser import ResumeParser
from backend.experience_engine.experience_engine import ExperienceEngine
from backend.skill_engine.skill_engine import SkillEngine
from backend.education_engine.education_engine import EducationEngine
from backend.project_engine.project_engine import ProjectEngine
from backend.certification_engine.certification_engine import CertificationEngine
from backend.candidate_profile.candidate_profile_engine import CandidateProfileEngine


class ResumePipeline:

    def __init__(self):

        self.parser = ResumeParser()

        self.experience_engine = ExperienceEngine()

        self.skill_engine = SkillEngine()

        self.education_engine = EducationEngine()

        self.project_engine = ProjectEngine()

        self.certification_engine = CertificationEngine()

        self.profile_engine = CandidateProfileEngine()


    def process_resume(self, file_path):

        parsed_result = self.parser.parse(file_path)

        if isinstance(parsed_result, dict):

            cleaned_text = (
                parsed_result.get("cleaned_text")
                or parsed_result.get("text")
                or parsed_result.get("raw_text")
                or ""
            )

        else:

            cleaned_text = parsed_result

        experience = self.experience_engine.extract(
            cleaned_text
        )

        skills = self.skill_engine.extract(
            cleaned_text
        )

        education = self.education_engine.extract(
            cleaned_text
        )

        projects = self.project_engine.extract(
            cleaned_text
        )

        certifications = self.certification_engine.extract(
            cleaned_text
        )
        candidate_profile = self.profile_engine.build(

            experience,

            skills,

            education,

            projects,

            certifications

        )
        return {

            "cleaned_text": cleaned_text,

            "experience": experience,

            "skills": skills,

            "education": education,

            "projects": projects,

            "certifications": certifications,

            "candidate_profile": candidate_profile

        }