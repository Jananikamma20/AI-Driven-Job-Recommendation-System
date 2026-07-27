from backend.resume_parser.parser import ResumeParser

from backend.project_engine.project_engine import ProjectEngine

parser = ResumeParser()

engine = ProjectEngine()

resume = parser.parse(

    "Data/Resumes/resume_pdfs/resume.pdf"

)

result = engine.extract(resume)

print("\nDetected Projects\n")

for project in result["projects"]:

    print(project)