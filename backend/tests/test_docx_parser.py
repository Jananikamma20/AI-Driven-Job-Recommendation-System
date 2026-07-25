import backend.resume_parser.docx_parser as dp

print(dp.__file__)
from backend.resume_parser.docx_parser import DOCXParser

parser = DOCXParser()

docx_path = "Data/Resumes/sample_resume.docx"

text = parser.extract_text(docx_path)

print(text)