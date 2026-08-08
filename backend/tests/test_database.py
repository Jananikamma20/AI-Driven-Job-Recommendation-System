from datetime import datetime
from backend.database.models import create_tables

from backend.database.operations import (
    insert_user,
    get_user,
    insert_resume,
    get_resume,
    insert_job,
    get_job,
    insert_recommendation,
    get_recommendation,
    get_recommendation_history
)


print("=" * 60)

print("DATABASE TEST")

print("=" * 60)


# ==========================================
# CREATE TABLES
# ==========================================

create_tables()

print()

print("Tables created successfully.")


# ==========================================
# INSERT USER
# ==========================================

unique_email = (
    f"test_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    "@example.com"
)

user_id = insert_user(

    "Test User",

    unique_email

)

print()

print("User ID:")

print(user_id)


# ==========================================
# GET USER
# ==========================================

user = get_user(user_id)

print()

print("User:")

print(user)


# ==========================================
# TEST RESUME
# ==========================================

resume_data = {

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


resume_id = insert_resume(

    user_id,

    "test_resume.pdf",

    resume_data

)

print()

print("Resume ID:")

print(resume_id)


resume = get_resume(resume_id)

print()

print("Resume:")

print(resume)


# ==========================================
# TEST JOB
# ==========================================

job_data = {

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


job_id = insert_job(

    "Data Analyst",

    "Google",

    job_data

)

print()

print("Job ID:")

print(job_id)


job = get_job(job_id)

print()

print("Job:")

print(job)


# ==========================================
# TEST RECOMMENDATION
# ==========================================

recommendation_data = {

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


recommendation_id = insert_recommendation(

    resume_id,

    job_id,

    recommendation_data

)

print()

print("Recommendation ID:")

print(recommendation_id)


recommendation = get_recommendation(

    recommendation_id

)

print()

print("Recommendation:")

print(recommendation)


# ==========================================
# HISTORY
# ==========================================

history = get_recommendation_history()

print()

print("Recommendation History:")

print(history)


print()

print("=" * 60)

print("DATABASE TEST COMPLETED")

print("=" * 60)