import os
import re
import pandas as pd

from backend.resume_parser.pdf_parser import PDFParser
from backend.resume_parser.docx_parser import DOCXParser
from backend.resume_parser.cleaner import ResumeCleaner


class ResumeParser:

    def __init__(self):

        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.cleaner = ResumeCleaner()
        
        self.skills_df = pd.read_csv("Data/KnowledgeBase/Skills/skills.csv")

        
        self.skills = set(
            self.skills_df["skill_name"]
            .dropna()
            .astype(str)
        )

        self.degrees_df = pd.read_csv("Data/KnowledgeBase/Education/degrees.csv")

        self.degrees = set(
            self.degrees_df["degree_name"]
            .dropna()
            .astype(str)
        )

        self.designations_df = pd.read_csv("Data/KnowledgeBase/Designations/designations.csv")

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

        self.certifications_df = pd.read_csv(
            "Data/KnowledgeBase/Certifications/certifications.csv",
            encoding="latin1"
        )

        self.certifications = set(
            self.certifications_df["certification_name"]
            .dropna()
            .astype(str)
        )

        self.courses_df = pd.read_csv(
            "Data/KnowledgeBase/Courses/courses.csv",
            encoding="cp1252"
        )

        self.courses = set(
            self.courses_df["course_name"]
            .dropna()
            .astype(str)
        )

        self.soft_skills_df = pd.read_csv(
            "Data/KnowledgeBase/SoftSkills/soft_skills.csv",
            encoding="latin1"
        )

        self.soft_skills = set(
            self.soft_skills_df["soft_skill"]
            .dropna()
            .astype(str)
        )

        

    # -------------------------
    # Extract Email
    # -------------------------
    def extract_email(self, text):

        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        emails = re.findall(pattern, text)

        return list(set(emails))

    # -------------------------
    # Extract Phone Number
    # -------------------------
    def extract_phone(self, text):

        pattern = r'(\+?\d{1,3}[\s-]?)?(\d{10})'

        matches = re.findall(pattern, text)

        phones = []

        for match in matches:

            country_code = match[0]
            number = match[1]

            phone = (country_code + number).strip()

            phones.append(phone)

        return list(set(phones))

    # -------------------------
    # Extract Skills
    # -------------------------
    def extract_skills(self, text):

        found_skills = []

        text_lower = text.lower()

        for skill in self.skills:

            pattern = r'\b' + re.escape(skill.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_skills.append(skill)
        return sorted(list(set(found_skills)))

    # -------------------------
    # Extract Degrees
    # -------------------------
    def extract_degrees(self, text):

        found_degrees = []

        text_lower = text.lower()

        for degree in self.degrees:

            pattern = r'\b' + re.escape(degree.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_degrees.append(degree)

        return sorted(list(set(found_degrees)))

    # -------------------------
    # Extract Designations
    # -------------------------
    def extract_designations(self, text):

        found_designations = []

        text_lower = text.lower()

        for designation in self.designations:

            pattern = r'\b' + re.escape(designation.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_designations.append(designation)

        return sorted(list(set(found_designations)))

    # -------------------------
    # Extract Companies
    # -------------------------
    def extract_companies(self, text):

        found_companies = []

        text_lower = text.lower()

        for company in self.companies:

            pattern = r'\b' + re.escape(company.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_companies.append(company)

        return sorted(list(set(found_companies)))

    # -------------------------
    # Extract Certifications
    # -------------------------
    def extract_certifications(self, text):

        found_certifications = []

        text_lower = text.lower()

        for certification in self.certifications:

            pattern = r'\b' + re.escape(certification.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_certifications.append(certification)

        return sorted(list(set(found_certifications)))

    # -------------------------
    # Extract Courses
    # -------------------------
    def extract_courses(self, text):

        found_courses = []

        text_lower = text.lower()

        for course in self.courses:

            pattern = r'\b' + re.escape(course.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_courses.append(course)

        return sorted(list(set(found_courses)))

    # -------------------------
    # Extract Soft Skills
    # -------------------------
    def extract_soft_skills(self, text):

        found_soft_skills = []

        text_lower = text.lower()

        for soft_skill in self.soft_skills:

            pattern = r'\b' + re.escape(soft_skill.lower()) + r'\b'

            if re.search(pattern, text_lower):

                found_soft_skills.append(soft_skill)

        return sorted(list(set(found_soft_skills)))

    # -------------------------
    # Parse Resume
    # -------------------------
    def parse(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":

            text = self.pdf_parser.extract_text(file_path)

        elif extension == ".docx":

            text = self.docx_parser.extract_text(file_path)

        else:

            raise ValueError("Unsupported file format.")

        # Clean Resume
        cleaned_text = self.cleaner.clean(text)

        # Extract Information
        email = self.extract_email(cleaned_text)

        phone = self.extract_phone(cleaned_text)

        skills = self.extract_skills(cleaned_text)

        degrees = self.extract_degrees(cleaned_text)

        designations = self.extract_designations(cleaned_text)

        companies = self.extract_companies(cleaned_text)

        certifications = self.extract_certifications(cleaned_text)

        courses = self.extract_courses(cleaned_text)

        soft_skills = self.extract_soft_skills(cleaned_text)

        # Return Result
        return {

            "file_name": os.path.basename(file_path),

            "file_type": extension,

            "cleaned_text": cleaned_text,

            "email": email,

            "phone": phone,

            "skills": skills,

            "degrees": degrees,

            "designations": designations,

            "companies": companies,

            "certifications": certifications,

            "courses": courses,

            "soft_skills": soft_skills

        }