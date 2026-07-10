from backend.experience_engine.company_detector import CompanyDetector

detector = CompanyDetector()

resume = """

Senior Software Engineer

Infosys

Worked on Cloud projects.

Software Engineer

Microsoft

Python Developer

Amazon

"""

companies = detector.extract(resume)

print()

print("Detected Companies")

print("-------------------")

for company in companies:

    print(company)