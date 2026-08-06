from backend.course_engine.course_engine import CourseEngine

engine = CourseEngine()

missing_skills = [

    "Python",

    "Power BI"

]

courses = engine.recommend_courses(

    missing_skills

)

print("=" * 60)
print("COURSE ENGINE TEST")
print("=" * 60)

for course in courses:

    print(course)