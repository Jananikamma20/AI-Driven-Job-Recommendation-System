#PDF Extraction Function
import pdfplumber

def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text

    return text

#Text Cleaning Function
import re

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9\s]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text

#Skill Extraction Function
def extract_skills(cleaned_text, skills_list):

    found_skills = []

    for skill in skills_list:

        if skill.lower() in cleaned_text:

            found_skills.append(skill)

    return list(set(found_skills))

#Experience Extraction Function
def extract_experience(cleaned_text):

    pattern = r'(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(20\d{2}|19\d{2})\s+to\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(20\d{2}|19\d{2})'

    matches = re.findall(
        pattern,
        cleaned_text,
        re.IGNORECASE
    )

    total_experience = 0

    for start, end in matches:

        total_experience += (
            int(end) - int(start)
        )

    return total_experience
