from backend.course_engine.course_engine import CourseEngine


print("=" * 60)
print("COURSE ENGINE TEST")
print("=" * 60)


engine = CourseEngine()


missing_skills = [
    "Machine Learning"
]


courses = engine.recommend_courses(
    missing_skills
)


print()
print("Missing Skills:")
print(missing_skills)


print()
print("Recommended Courses:")
print(courses)


print()
print("Total Courses:")
print(len(courses))