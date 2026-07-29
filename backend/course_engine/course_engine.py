from backend.course_engine.course_recommender import CourseRecommender
from backend.course_engine.course_validator import CourseValidator


class CourseEngine:

    def __init__(self):

        self.recommender = CourseRecommender()

        self.validator = CourseValidator()


    def recommend(self, missing_skills):

        courses = self.recommender.recommend(

            missing_skills

        )

        courses = self.validator.validate(

            courses

        )

        return courses