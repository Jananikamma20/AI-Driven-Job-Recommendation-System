import re
class DesignationDetector:

    def __init__(self):

        self.designations = [

            "Software Engineer",

            "Senior Software Engineer",

            "Principal Software Engineer",

            "Engineering Manager",

            "Software Architect",

            "Backend Developer",

            "Frontend Developer",

            "Full Stack Developer",

            "Data Scientist",

            "Machine Learning Engineer",

            "AI Engineer",

            "DevOps Engineer",

            "Cloud Engineer",

            "Python Developer",

            "Java Developer",

            "Android Developer",

            "Project Manager",

            "Business Analyst",

            "System Analyst",

            "QA Engineer",

            "Test Engineer"

        ]
        

    def extract(self, resume_text):

        found = []

        for designation in self.designations:

            pattern = r"\b" + re.escape(designation) + r"\b"

            if re.search(

                pattern,

                resume_text,

                re.IGNORECASE

            ):

                found.append(

                    designation

                )

        return sorted(

            list(

                set(found)

            )

        )