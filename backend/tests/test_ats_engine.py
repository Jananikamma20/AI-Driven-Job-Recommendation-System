from backend.ats_engine.ats_engine import ATSEngine

engine = ATSEngine()

candidate = {

    "education": {

        "normalized_degrees": [

            "Bachelor of Technology"

        ]

    },

    "projects": {

        "projects": [

            "Project 1",

            "Project 2"

        ]

    },

    "certifications": {

        "certifications": [

            "AWS",

            "NPTEL"

        ]

    }

}

skill_gap = {

    "matched_skills": [

        "python",

        "sql",

        "tableau"

    ],

    "missing_skills": [

        "docker",

        "aws"

    ]

}

score = engine.calculate(

    candidate,

    skill_gap

)

print()

print("ATS SCORE :", score)