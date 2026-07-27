from backend.project_engine.project_detector import ProjectDetector
from backend.project_engine.project_validator import ProjectValidator


class ProjectEngine:

    def __init__(self):

        self.detector = ProjectDetector()

        self.validator = ProjectValidator()


    def extract(self, resume_text):

        detected_projects = self.detector.extract(
            resume_text
        )

        valid_projects, invalid_projects = (

            self.validator.validate(
                detected_projects
            )

        )

        return {

            "projects": valid_projects,

            "invalid_projects": invalid_projects

        }