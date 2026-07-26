from backend.resume_parser.parser import ResumeParser
from backend.skill_engine.skill_engine import SkillEngine

parser = ResumeParser()

engine = SkillEngine()

resume = parser.parse(
    "Data/Resumes/resume_pdfs/ENGINEERING/54227873.pdf"
)

result = engine.extract(resume)

print("\n==============================")
print("DETECTED SKILLS")
print("==============================")

for skill in result["detected_skills"]:

    print(skill)

print("\n==============================")
print("NORMALIZED SKILLS")
print("==============================")

for skill in result["normalized_skills"]:

    print(skill)