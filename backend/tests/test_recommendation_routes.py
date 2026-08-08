import requests


url = "http://127.0.0.1:5000/analyze-recommendation"


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
        "Data Analyst job requiring Python, SQL, Power BI and Machine Learning."
}


payload = {

    "user_id": 1,

    "resume": resume,

    "job": job,

    "resume_file_name": "test_resume.pdf"

}


print("=" * 60)

print("VERSION 2 RECOMMENDATION ROUTE TEST")

print("=" * 60)


response = requests.post(

    url,

    json=payload

)


print()

print("STATUS CODE")

print(response.status_code)


print()

print("RESPONSE")

print(response.json())


print()

print("=" * 60)

print("TEST COMPLETED")

print("=" * 60)