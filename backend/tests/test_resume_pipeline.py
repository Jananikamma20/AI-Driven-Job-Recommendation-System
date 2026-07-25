from backend.resume_parser.parser import ResumeParser
from backend.experience_engine.company_detector import CompanyDetector
from backend.experience_engine.designation_detector import DesignationDetector
from backend.experience_engine.date_detector import DateDetector

parser = ResumeParser()

text = parser.parse("Data/Resumes/resume_pdfs/ACCOUNTANT/10554236.pdf")

print("\n========= CLEANED TEXT =========\n")
print(text)

print("\n========= COMPANIES =========")
print(CompanyDetector().extract(text))

print("\n========= DESIGNATIONS =========")
print(DesignationDetector().extract(text))

print("\n========= DATES =========")
print(DateDetector().detect_dates(text))