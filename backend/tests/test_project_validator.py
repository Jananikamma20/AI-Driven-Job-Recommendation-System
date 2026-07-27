from backend.project_engine.project_validator import ProjectValidator

validator = ProjectValidator()

projects = [

    "Real-Time Stock Analysis Dashboard",

    "AI",

    "",

    "Customer Segmentation Using K-Means"

]

valid_projects, invalid_projects = validator.validate(projects)

print("\nValid Projects\n")

for project in valid_projects:

    print(project)

print("\nInvalid Projects\n")

for project in invalid_projects:

    print(project)