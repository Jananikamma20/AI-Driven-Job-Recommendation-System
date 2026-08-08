from datetime import datetime
from backend.database.models import create_tables

from backend.database.operations import (
    insert_user,
    get_recommendation
)

from backend.Services.recommendation_service import (
    RecommendationService
)


print("=" * 60)

print("RECOMMENDATION SERVICE TEST")

print("=" * 60)


# ==========================================
# CREATE DATABASE TABLES
# ==========================================

create_tables()


# ==========================================
# CREATE USER
# ==========================================

unique_email = (

    f"integration_test_"
    f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
    "@example.com"

)

user_id = insert_user(

    "Integration Test User",

    unique_email

)


# ==========================================
# RESUME
# ==========================================

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


# ==========================================
# JOB
# ==========================================

job = {

    "title":

        "Data Analyst",

    "company":

        "Google",

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

        "4 years"

    ],

    "certifications": [

        "IBM Data Science"

    ],

    "description":

        "Data Analyst job"

}


# ==========================================
# RUN SERVICE
# ==========================================

service = RecommendationService()


result = service.analyze_and_save(

    user_id,

    resume,

    job,

    "integration_test.pdf"

)


# ==========================================
# PRINT RESULT
# ==========================================

print()

print("STATUS")

print(result.get("status"))


print()

print("MESSAGE")

print(result.get("message"))


print()

print("SUMMARY")

print(result.get("summary"))


print()

print("DATABASE")

print(result.get("database"))


# ==========================================
# VERIFY DATABASE
# ==========================================

recommendation_id = (

    result["database"]

    ["recommendation_id"]

)


saved = get_recommendation(

    recommendation_id

)


print()

print("SAVED RECOMMENDATION")

print(saved)


print()

print("=" * 60)

print("RECOMMENDATION SERVICE TEST COMPLETED")

print("=" * 60)

history = service.get_history()

print()

print("RECOMMENDATION HISTORY")

print(history)