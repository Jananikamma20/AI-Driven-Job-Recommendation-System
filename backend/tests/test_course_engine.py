from backend.course_engine.course_engine import CourseEngine

engine = CourseEngine()

missing_skills = [

    "aws",

    "docker",

    "machine learning",

    "power bi"

]

courses = engine.recommend(

    missing_skills

)

print("\nRecommended Courses\n")

for skill, course in courses.items():

    print(f"{skill} --> {course}")