from backend.ats_engine.ats_calculator import ATSCalculator

calculator = ATSCalculator()

candidate = {

    "education": {

        "normalized_degrees":[

            "Bachelor of Technology"

        ]

    },

    "projects": {

        "projects":[

            "Project1",

            "Project2"

        ]

    },

    "certifications": {

        "certifications":[

            "AWS",

            "NPTEL"

        ]

    }

}

skill_gap = {

    "matched_skills":[

        "python",

        "sql",

        "tableau"

    ],

    "missing_skills":[

        "aws",

        "docker"

    ]

}

score = calculator.calculate(

    candidate,

    skill_gap

)

print()

print("ATS SCORE :", score)