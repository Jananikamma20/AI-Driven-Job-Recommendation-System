from backend.matching_engine.matcher import ResumeJobMatcher

matcher = ResumeJobMatcher()

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

    "skills": [

        "Python",
        "SQL",
        "Pandas",
        "Power BI"

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

print("=" * 60)
print("MATCHING ENGINE TEST")
print("=" * 60)

result = matcher.match(resume, job)

print("\nMatch Score")
print(result["match_score"])

print("\nMatched Skills")
print(result["matched_skills"])

print("\nMissing Skills")
print(result["missing_skills"])

print("\nDegree Match")
print(result["degree_match"])

print("\nExperience Match")
print(result["experience_match"])

print("\nCertification Match")
print(result["certification_match"])