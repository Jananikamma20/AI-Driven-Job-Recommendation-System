from backend.resume_parser.parser import ResumeParser
from backend.skill_engine.skill_detector import SkillDetector

parser = ResumeParser()

detector = SkillDetector()

resume = parser.parse(
    "Data/Resumes/resume_pdfs/ACCOUNTANT/10554236.pdf"
)

skills = detector.detect(resume)

print("\nDetected Skills\n")

for skill in skills:

    print(skill)