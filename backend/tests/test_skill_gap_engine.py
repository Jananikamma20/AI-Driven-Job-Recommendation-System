from backend.skill_gap_engine.skill_gap_engine import SkillGapEngine

engine = SkillGapEngine()

candidate = {

    "skills": {

        "normalized_skills":[

            "Python",

            "SQL",

            "Tableau"

        ]

    }

}

job_description = """

Need Python developer.

Must know SQL.

Docker

AWS

Machine Learning

"""

result = engine.analyze(

    candidate,

    job_description

)

print(result)