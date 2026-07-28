class RecommendationValidator:

    def __init__(self):

        pass


    def validate(self, recommendations):

        valid = []

        invalid = []

        for recommendation in recommendations:

            if recommendation["score"] > 0:

                valid.append(recommendation)

            else:

                invalid.append(recommendation)

        return valid, invalid