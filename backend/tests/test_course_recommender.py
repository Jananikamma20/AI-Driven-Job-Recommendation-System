from backend.course_engine.course_recommender import CourseRecommender

recommender = CourseRecommender()

missing_skills = [

    "aws",

    "docker",

    "power bi",

    "machine learning"

]

courses = recommender.recommend(

    missing_skills

)

print("\nRecommended Courses\n")

for skill, course in courses.items():

    print(f"{skill} --> {course}")