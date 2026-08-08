from datetime import datetime
from backend.database.models import create_tables

from backend.database.operations import (
    insert_user,
    get_recommendation
)

from backend.database.recommendation_storage import (
    RecommendationStorage
)


print("=" * 60)

print("RECOMMENDATION STORAGE TEST")

print("=" * 60)


# Create tables

create_tables()


# Create test user

unique_email = (

    f"storage_test_"
    f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    "@example.com"

)

user_id = insert_user(

    "Storage Test User",

    unique_email

)


# Resume

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

        "4 years"

    ],

    "certifications": [

        "IBM Data Science"

    ],

    "projects": [

        "Stock Analysis Dashboard"

    ]

}


# Job

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

        "4 years"

    ],

    "certifications": [

        "IBM Data Science"

    ],

    "description":

        "Data Analyst job"

}


# Recommendation result

recommendation = {

    "status": "success",

    "message":

        "Recommendation generated successfully.",

    "summary": {

        "overall_match": 65.0,

        "ats_score": 65.0,

        "recommendation":

            "Recommended"

    },

    "statistics": {

        "matched_skills": 2,

        "missing_skills": 2,

        "recommended_courses": 14

    }

}


# Save everything

storage = RecommendationStorage()


result = storage.save_analysis(

    user_id,

    resume,

    job,

    recommendation,

    "test_resume.pdf"

)


print()

print("STORAGE RESULT")

print(result)


# Retrieve recommendation

saved = get_recommendation(

    result["recommendation_id"]

)


print()

print("SAVED RECOMMENDATION")

print(saved)


print()

print("=" * 60)

print("RECOMMENDATION STORAGE TEST COMPLETED")

print("=" * 60)