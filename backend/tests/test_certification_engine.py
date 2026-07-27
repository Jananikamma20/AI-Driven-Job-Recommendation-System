from backend.resume_parser.parser import ResumeParser

from backend.certification_engine.certification_engine import CertificationEngine

parser = ResumeParser()

engine = CertificationEngine()

resume = parser.parse(

    "Data/Resumes/resume_pdfs/resume.pdf"

)

result = engine.extract(resume)

print("\nDetected Certifications\n")

for certification in result["certifications"]:

    print(certification)