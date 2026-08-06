class SkillNormalizer:

    def __init__(self):

        pass

    def normalize(self, skills):

        if not skills:

            return []

        normalized = []

        for skill in skills:

            normalized.append(
                skill.strip().lower()
            )

        return sorted(
            list(set(normalized))
        )