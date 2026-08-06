from backend.education_engine.education_engine import EducationEngine

engine = EducationEngine()

resume = {

    "degrees": [

        "B.Tech",

        "MCA"

    ]

}

job = {

    "degrees": [

        "B.Tech",

        "MBA"

    ]

}

result = engine.analyze(

    resume,

    job

)

print("=" * 60)
print("EDUCATION ENGINE TEST")
print("=" * 60)

print()

print("Education Match")
print(result["education_match"])

print()

print("Matched Degrees")
print(result["matched_degrees"])

print()

print("Missing Degrees")
print(result["missing_degrees"])

print()

print("Education Score")
print(result["education_score"])