class CourseValidator:

    def __init__(self):

        pass


    def validate(self, courses):

        validated_courses = {}

        seen = set()

        for skill, course in courses.items():

            if course not in seen:

                validated_courses[skill] = course

                seen.add(course)

        return validated_courses