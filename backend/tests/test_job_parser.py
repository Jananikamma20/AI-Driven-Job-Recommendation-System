from backend.job_parser.parser import JobParser

parser = JobParser()

job_summary = """
Google is hiring a Data Analyst.

Qualification:
B.Tech or MCA

Experience:
2-4 years
"""

job_skills = """
Python
SQL
Pandas
Tableau
"""

result = parser.parse_job(job_summary, job_skills)

print(result)