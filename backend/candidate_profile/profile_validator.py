class ProfileValidator:

    def __init__(self):

        pass

    def validate(self, profile):

        valid = {}

        invalid = {}

        for key, value in profile.items():

            if value:

                valid[key] = value

            else:

                invalid[key] = value

        return valid, invalid