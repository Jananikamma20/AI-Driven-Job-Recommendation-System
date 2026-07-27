class ProjectValidator:

    def __init__(self):

        pass


    def validate(self, projects):

        valid_projects = []

        invalid_projects = []

        for project in projects:

            if len(project.strip()) >= 5:

                valid_projects.append(project)

            else:

                invalid_projects.append(project)

        return valid_projects, invalid_projects