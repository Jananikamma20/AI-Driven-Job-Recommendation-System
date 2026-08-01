import requests

url = "http://127.0.0.1:5000/recommend-jobs"

resume_path = "Data/Resumes/resume_pdfs/resume.pdf"

with open(resume_path, "rb") as file:

    files = {
        "resume": file
    }

    response = requests.post(
        url,
        files=files
    )

print("Status Code:", response.status_code)

data = response.json()

recommendations = data["recommendations"]["recommended_jobs"]

print("\nTop Recommended Jobs:\n")

for i, recommendation in enumerate(recommendations, start=1):

    print("=" * 60)
    print("Rank :", i)
    print("Score:", recommendation["score"])

    job = recommendation["job"]

    print("Job Link:", job["job_link"])

    print("Summary:")
    print(job["job_summary"][:300] + "...")