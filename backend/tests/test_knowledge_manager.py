from backend.knowledgebase.knowledge_manager import KnowledgeManager

manager = KnowledgeManager()

print(manager.skills.columns)

print(manager.education.columns)

print(manager.companies.columns)

print(manager.jobs.columns)