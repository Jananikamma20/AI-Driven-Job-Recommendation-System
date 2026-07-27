class CertificationValidator:

    def __init__(self):

        pass

    def validate(self, certifications):

        valid = []

        invalid = []

        for certification in certifications:

            if len(certification.strip()) >= 3:

                valid.append(

                    certification

                )

            else:

                invalid.append(

                    certification

                )

        return valid, invalid