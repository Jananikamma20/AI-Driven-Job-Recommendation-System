from backend.ats_engine.ats_engine import ATSEngine

engine = ATSEngine()

resume = {

    "skills": [

        "Python",

        "SQL",

        "Pandas"

    ],

    "degrees": [

        "B.Tech"

    ],

    "experience": [

        "2-4 years"

    ],

    "certifications": [

        "IBM Data Science"

    ]

}

job = {

    "title": "Data Analyst",

    "company": "Google",

    "skills": [

        "Python",

        "SQL",

        "Power BI",

        "Machine Learning"

    ],

    "degrees": [

        "B.Tech"

    ],

    "experience": [

        "2-4 years"

    ],

    "certifications": [

        "IBM Data Science"

    ]

}

result = engine.calculate_ats_score(

    resume,

    job

)

print("=" * 60)
print("ATS ENGINE TEST")
print("=" * 60)

print()

print("ATS Score")
print(result["ats_score"])

print()

print("Rating")
print(result["rating"])

print()

print("Missing Keywords")
print(result["missing_keywords"])

print()

print("Suggestions")

for suggestion in result["suggestions"]:

    print("-", suggestion)