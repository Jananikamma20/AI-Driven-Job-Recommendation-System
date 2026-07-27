import re


class CertificationDetector:

    def __init__(self):

        self.certifications = [

            "AWS",

            "Microsoft",

            "Azure",

            "Google",

            "Oracle",

            "Cisco",

            "IBM",

            "NPTEL",

            "Coursera",

            "Udemy",

            "edX",

            "Infosys Springboard",

            "Salesforce",

            "Red Hat",

            "CCNA",

            "CCNP",

            "RHCE",

            "TensorFlow Developer",

            "Data Analytics",

            "Machine Learning"

        ]


    def extract(self, resume_text):

        found = []

        for certification in self.certifications:

            pattern = r"\b" + re.escape(certification) + r"\b"

            if re.search(

                pattern,

                resume_text,

                re.IGNORECASE

            ):

                found.append(

                    certification

                )

        return sorted(

            list(

                set(found)

            )

        )