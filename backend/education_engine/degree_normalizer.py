class DegreeNormalizer:

    def __init__(self):

        self.mapping = {

            "b.tech": "Bachelor of Technology",
            "b tech": "Bachelor of Technology",
            "bachelor of technology": "Bachelor of Technology",

            "b.e": "Bachelor of Engineering",
            "be": "Bachelor of Engineering",
            "bachelor of engineering": "Bachelor of Engineering",

            "b.sc": "Bachelor of Science",
            "bsc": "Bachelor of Science",
            "bachelor of science": "Bachelor of Science",

            "m.tech": "Master of Technology",
            "m tech": "Master of Technology",
            "master of technology": "Master of Technology",

            "m.sc": "Master of Science",
            "msc": "Master of Science",
            "master of science": "Master of Science",

            "mba": "Master of Business Administration",

            "mca": "Master of Computer Applications",

            "bca": "Bachelor of Computer Applications",

            "phd": "Doctor of Philosophy",

            "diploma": "Diploma"

        }


    def normalize(self, degrees):

        normalized = []

        for degree in degrees:

            key = degree.lower().strip()

            if key in self.mapping:

                normalized.append(

                    self.mapping[key]

                )

            else:

                normalized.append(

                    degree

                )

        return sorted(

            list(

                set(normalized)

            )

        )