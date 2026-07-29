from backend.course_engine.course_validator import CourseValidator

validator = CourseValidator()

courses = {

    "aws": "AWS Cloud Practitioner",

    "cloud": "AWS Cloud Practitioner",

    "docker": "Docker for Beginners"

}

validated = validator.validate(

    courses

)

print(validated)