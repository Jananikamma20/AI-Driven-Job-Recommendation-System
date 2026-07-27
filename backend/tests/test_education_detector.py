from backend.resume_parser.parser import ResumeParser
from backend.education_engine.education_detector import EducationDetector

parser = ResumeParser()

detector = EducationDetector()

resume = parser.parse(
    "Data/Resumes/resume_pdfs/ENGINEERING/54227873.pdf"
)

degrees = detector.extract(resume)

print("\nDetected Degrees\n")

for degree in degrees:

    print(degree)