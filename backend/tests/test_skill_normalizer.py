from backend.skill_engine.skill_normalizer import SkillNormalizer

normalizer = SkillNormalizer()

skills = [

    "Python",
    "py",
    "ML",
    "Machine Learning",
    "JS",
    "JavaScript",
    "Tensor Flow",
    "tensorflow",
    "Scikit Learn",
    "SQL Server"

]

result = normalizer.normalize(skills)

print("\nNormalized Skills\n")

for skill in result:

    print(skill)