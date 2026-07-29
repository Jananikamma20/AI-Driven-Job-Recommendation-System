class SkillGapAnalyzer:

    def __init__(self):

        pass


    def analyze(

        self,

        candidate_profile,

        job_description

    ):

        candidate_skills = []

        if "normalized_skills" in candidate_profile["skills"]:

            candidate_skills = [

                skill.lower()

                for skill in

                candidate_profile["skills"]["normalized_skills"]

            ]

        matched = []

        missing = []

        text = job_description.lower()

        for skill in candidate_skills:

            if skill in text:

                matched.append(skill)

        important_skills = [

            "python",

            "sql",

            "java",

            "tableau",

            "power bi",

            "aws",

            "docker",

            "kubernetes",

            "machine learning",

            "deep learning"

        ]

        for skill in important_skills:

            if skill in text and skill not in matched:

                missing.append(skill)

        return {

            "matched_skills": matched,

            "missing_skills": missing

        }