import re


class EducationDetector:

    def __init__(self):

        self.degrees = [

            "Bachelor of Technology",
            "Bachelor of Engineering",
            "Bachelor of Science",
            "Bachelor of Computer Applications",
            "Master of Technology",
            "Master of Science",
            "Master of Computer Applications",
            "Bachelor of Arts",
            "Master of Arts",
            "Bachelor of Commerce",
            "Master of Commerce",

            "B.Tech",
            "B.E",
            "B.Sc",
            "BCA",
            "M.Tech",
            "M.Sc",
            "MCA",
            "B.Com",
            "M.Com",

            "MBA",
            "PhD",
            "Diploma"

        ]


    def extract(self, resume_text):

        found = []

        for degree in self.degrees:

            pattern = r"\b" + re.escape(degree) + r"\b"

            if re.search(

                pattern,

                resume_text,

                re.IGNORECASE

            ):

                found.append(degree)

        return sorted(

            list(

                set(found)

            )

        )