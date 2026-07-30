class ATSValidator:

    def __init__(self):

        pass


    def validate(self, score):

        if score < 0:
            score = 0

        elif score > 100:
            score = 100

        return round(score, 2)