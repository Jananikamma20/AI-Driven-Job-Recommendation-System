from backend.resume_parser.parser import ResumeParser

from backend.project_engine.project_detector import ProjectDetector

parser = ResumeParser()

detector = ProjectDetector()

resume = parser.parse(

    "Data/Resumes/resume_pdfs/resume.pdf"

)

projects = detector.extract(resume)

print("\nDetected Projects\n")

for project in projects:

    print(project)