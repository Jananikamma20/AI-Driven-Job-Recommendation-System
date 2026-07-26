from backend.skill_engine.skill_loader import SkillLoader

loader = SkillLoader()

skills = loader.load("KnowledgeBase/skills.csv")

print("\nTOTAL SKILLS:", len(skills))

print("\nFIRST 20 SKILLS:\n")

for skill in skills[:20]:

    print(skill)