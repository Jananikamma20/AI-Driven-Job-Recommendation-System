class SkillNormalizer:

    def __init__(self):

        self.mapping = {

            "ml": "Machine Learning",
            "machine learning": "Machine Learning",

            "ai": "Artificial Intelligence",
            "artificial intelligence": "Artificial Intelligence",

            "dl": "Deep Learning",
            "deep learning": "Deep Learning",

            "py": "Python",
            "python": "Python",

            "js": "JavaScript",
            "javascript": "JavaScript",

            "tf": "TensorFlow",
            "tensor flow": "TensorFlow",
            "tensorflow": "TensorFlow",

            "scikit learn": "Scikit-learn",
            "scikit-learn": "Scikit-learn",

            "sql server": "SQL",
            "mysql": "MySQL",
            "postgresql": "PostgreSQL"
        }


    def normalize(self, skills):

        normalized = []

        for skill in skills:

            key = skill.lower().strip()

            if key in self.mapping:

                normalized.append(

                    self.mapping[key]

                )

            else:

                normalized.append(

                    skill

                )

        return sorted(

            list(

                set(normalized)

            )

        )