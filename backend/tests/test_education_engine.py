from backend.resume_parser.parser import ResumeParser
from backend.education_engine.education_engine import EducationEngine

parser = ResumeParser()

engine = EducationEngine()

resume = parser.parse(
    "Data/Resumes/resume_pdfs/ENGINEERING/54227873.pdf"
)

result = engine.extract(resume)

print("\n==============================")
print("DETECTED DEGREES")
print("==============================")

for degree in result["detected_degrees"]:

    print(degree)

print("\n==============================")
print("NORMALIZED DEGREES")
print("==============================")

for degree in result["normalized_degrees"]:

    print(degree)