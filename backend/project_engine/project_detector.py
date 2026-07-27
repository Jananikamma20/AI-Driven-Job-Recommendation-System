import re


class ProjectDetector:

    def __init__(self):

        self.start_keywords = [

            "projects",
            "project",
            "academic projects",
            "major projects",
            "minor projects",
            "internship projects",
            "capstone projects"

        ]

        self.end_keywords = [

            "skills",
            "education",
            "experience",
            "certifications",
            "certification",
            "languages",
            "activities",
            "interests",
            "achievements",
            "awards",
            "personal information",
            "references"

        ]


    def extract(self, resume_text):

        text = resume_text.lower()

        start = -1

        for keyword in self.start_keywords:

            if keyword in text:

                start = text.find(keyword)

                break

        if start == -1:

            return []

        end = len(text)

        for keyword in self.end_keywords:

            pos = text.find(keyword, start + 10)

            if pos != -1 and pos < end:

                end = pos

        project_section = resume_text[start:end].strip()

        return [project_section]