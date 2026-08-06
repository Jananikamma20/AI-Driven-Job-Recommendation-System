from backend.experience_engine.experience_engine import ExperienceEngine

engine = ExperienceEngine()

resume = {

    "experience": [

        "3+ years"

    ]

}

job = {

    "experience": [

        "2-4 years"

    ]

}

result = engine.analyze(

    resume,

    job

)

print("=" * 60)
print("EXPERIENCE ENGINE TEST")
print("=" * 60)

print()

print("Resume Years")
print(result["resume_years"])

print()

print("Job Years")
print(result["job_years"])

print()

print("Experience Match")
print(result["experience_match"])

print()

print("Experience Score")
print(result["experience_score"])