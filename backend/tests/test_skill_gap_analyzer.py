from backend.skill_gap_engine.skill_gap_analyzer import SkillGapAnalyzer

analyzer = SkillGapAnalyzer()

candidate = {

    "skills": {

        "normalized_skills": [

            "Python",

            "SQL",

            "Tableau"

        ]

    }

}

job_description = """

Looking for Python developer.

Must know SQL.

Experience with Docker,

AWS,

Power BI,

Machine Learning.

"""

result = analyzer.analyze(

    candidate,

    job_description

)

print(result)