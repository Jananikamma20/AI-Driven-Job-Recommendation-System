from backend.project_engine.project_engine import ProjectEngine

engine = ProjectEngine()

resume_projects = [

    "Stock Analysis Dashboard",

    "Customer Segmentation using K-Means",

    "Weather Forecast App"

]

job_text = """

We are looking for candidates having experience in

Stock Analysis Dashboard,

Python,

SQL,

Machine Learning,

Power BI.

"""

result = engine.match_projects(

    resume_projects,

    job_text

)

print("=" * 60)
print("PROJECT ENGINE TEST")
print("=" * 60)

print()

print("Matched Projects")
print(result["matched_projects"])

print()

print("Missing Projects")
print(result["missing_projects"])

print()

print("Project Score")
print(result["project_score"])