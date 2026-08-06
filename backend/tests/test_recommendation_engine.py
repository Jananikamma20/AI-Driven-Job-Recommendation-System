from backend.recommendation_engine.recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

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

    ],

    "projects": [

        "Stock Analysis Dashboard"

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

    ],

    "description": """

    Looking for candidates with experience in

    Stock Analysis Dashboard,

    Power BI,

    Machine Learning.

    """

}

result = engine.analyze(

    resume,

    job

)

print("=" * 60)
print("RECOMMENDATION ENGINE TEST")
print("=" * 60)

for key, value in result.items():

    print()

    print(key.upper())

    print(value)