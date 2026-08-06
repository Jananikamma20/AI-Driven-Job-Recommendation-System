import re
import pandas as pd

class JobParser:

    def __init__(self):
        self.skills_df = pd.read_csv(
            "Data/KnowledgeBase/Skills/skills.csv"
        )

        self.skills = set(
            self.skills_df["skill_name"]
            .dropna()
            .astype(str)
        )

        self.degrees_df = pd.read_csv(
            "Data/KnowledgeBase/Education/degrees.csv"
        )

        self.degrees = set(
            self.degrees_df["degree_name"]
            .dropna()
            .astype(str)
        )

        self.designations_df = pd.read_csv(
            "Data/KnowledgeBase/Designations/designations.csv"
        )

        self.designations = set(
            self.designations_df["designation_name"]
            .dropna()
            .astype(str)
        )

        self.companies_df = pd.read_csv(
            "Data/KnowledgeBase/Companies/companies.csv",
            encoding="cp1252"
        )

        self.companies = set(
            self.companies_df["company_name"]
            .dropna()
            .astype(str)
        )

    def extract_skills(self, text):

        if not text:
            return []

        found_skills = []

        text_lower = text.lower()

        for skill in self.skills:

            pattern = r'\b' + re.escape(skill.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_skills.append(skill)

        return sorted(list(set(found_skills)))

    def extract_degrees(self, text):

        if not text:
            return []

        found_degrees = []

        text_lower = text.lower()

        for degree in self.degrees:

            pattern = r'\b' + re.escape(degree.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_degrees.append(degree)

        return sorted(list(set(found_degrees)))

    def extract_designations(self, text):

        if not text:
            return []

        found_designations = []

        text_lower = text.lower()

        for designation in self.designations:

            pattern = r'\b' + re.escape(designation.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_designations.append(designation)

        return sorted(list(set(found_designations)))

    def extract_companies(self, text):

        if not text:
            return []

        found_companies = []

        text_lower = text.lower()

        for company in self.companies:

            pattern = r'\b' + re.escape(company.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_companies.append(company)

        return sorted(list(set(found_companies)))

    def extract_experience(self, text):

        patterns = [

            r'\d+\+?\s*years?',

            r'\d+\+?\s*yrs?',

            r'\d+\s*-\s*\d+\s*years?',

            r'\d+\s*-\s*\d+\s*yrs?',

            r'\d+\s*to\s*\d+\s*years?',

            r'freshers?'

        ]

        experiences = []

        text_lower = text.lower()

        for pattern in patterns:

            matches = re.findall(pattern, text_lower)

            experiences.extend(matches)

        return list(set(experiences))

    def parse_job(self, job_summary, job_skills):

        text = str(job_summary) + "\n" + str(job_skills)

        skills = self.extract_skills(text)

        degrees = self.extract_degrees(text)

        designations = self.extract_designations(text)

        companies = self.extract_companies(text)

        experience = self.extract_experience(text)

        return {

            "skills": skills,

            "degrees": degrees,

            "designations": designations,

            "companies": companies,

            "experience": experience

        }