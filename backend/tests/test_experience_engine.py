from backend.experience_engine.experience_engine import ExperienceEngine

resume = """
Microsoft
Software Engineer
Jan 2018 - Jul 2020

Infosys
Senior Software Engineer
Aug 2020 - Present
"""

engine = ExperienceEngine()

result = engine.extract(resume)

print(result)