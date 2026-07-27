from backend.resume_parser.parser import ResumeParser

from backend.certification_engine.certification_detector import CertificationDetector

parser = ResumeParser()

detector = CertificationDetector()

resume = parser.parse(

    "Data/Resumes/resume_pdfs/resume.pdf"

)

result = detector.extract(resume)

print("\nDetected Certifications\n")

for certification in result:

    print(certification)