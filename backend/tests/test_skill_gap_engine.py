from backend.skill_gap_engine.skill_gap_engine import SkillGapEngine

engine = SkillGapEngine()

matching_result = {

    "match_score": 82.5,

    "matched_skills": [

        "Python",

        "SQL",

        "Pandas"

    ],

    "missing_skills": [

        "Power BI",

        "Machine Learning"

    ]

}

result = engine.analyze_skill_gap(

    matching_result

)

print("=" * 60)

print("SKILL GAP ENGINE TEST")

print("=" * 60)

print()

print("Gap Percentage")

print(result["gap_percentage"])

print()

print("Priority")

print(result["priority"])

print()

print("Recommendations")

print(result["recommendations"])