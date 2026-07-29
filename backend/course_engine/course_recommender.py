class CourseRecommender:

    def __init__(self):

        self.course_catalog = {

            "python": "Python for Everybody",

            "sql": "SQL for Data Analysis",

            "tableau": "Tableau Desktop Specialist",

            "power bi": "Microsoft Power BI Essentials",

            "aws": "AWS Cloud Practitioner",

            "docker": "Docker for Beginners",

            "kubernetes": "Kubernetes Fundamentals",

            "machine learning": "Machine Learning by Andrew Ng",

            "deep learning": "Deep Learning Specialization",

            "java": "Java Programming Masterclass"

        }


    def recommend(self, missing_skills):

        recommendations = {}

        for skill in missing_skills:

            key = skill.lower()

            if key in self.course_catalog:

                recommendations[skill] = self.course_catalog[key]

        return recommendations