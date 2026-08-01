import requests

url = "http://127.0.0.1:5000/upload-resume"

resume_path = "Data/Resumes/resume_pdfs/resume.pdf"

with open(resume_path, "rb") as file:
    files = {
        "resume": file
    }

    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)