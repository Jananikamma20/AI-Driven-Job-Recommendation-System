from backend.skill_gap_engine.skill_gap_validator import SkillGapValidator

validator = SkillGapValidator()

result = {

    "matched_skills":[

        "python",

        "python",

        "sql"

    ],

    "missing_skills":[

        "aws",

        "docker",

        "aws"

    ]

}

validated = validator.validate(result)

print(validated)