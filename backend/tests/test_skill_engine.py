from backend.skill_engine.skill_engine import SkillEngine

engine = SkillEngine()

resume = {

    "skills": [

        "Python",

        "SQL",

        "Pandas"

    ]

}

job = {

    "skills": [

        "Python",

        "SQL",

        "Pandas",

        "Power BI",

        "Machine Learning"

    ]

}

result = engine.analyze(

    resume,

    job

)

print("=" * 60)
print("SKILL ENGINE TEST")
print("=" * 60)

print()

print("Total Resume Skills")
print(result["total_resume_skills"])

print()

print("Total Job Skills")
print(result["total_job_skills"])

print()

print("Matched Skills")
print(result["matched_skills"])

print()

print("Missing Skills")
print(result["missing_skills"])

print()

print("Skill Score")
print(result["skill_score"])