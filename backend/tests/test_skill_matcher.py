from backend.skill_engine.skill_matcher import SkillMatcher

matcher = SkillMatcher()

candidate_skills = [

    "Python",
    "SQL",
    "Machine Learning",
    "Pandas",
    "TensorFlow"

]

job_skills = [

    "Python",
    "SQL",
    "AWS",
    "Docker",
    "Machine Learning"

]

result = matcher.match(

    candidate_skills,

    job_skills

)

print("\nMatched Skills")

print(result["matched_skills"])

print("\nMissing Skills")

print(result["missing_skills"])

print("\nMatch Percentage")

print(result["match_percentage"], "%")