from datetime import datetime


class ExperienceCalculator:

    def __init__(self):

        self.today = datetime.today()


    def calculate(self, start_date, end_date):

        """
        Calculate total experience.

        Input

        2020-08
        Present

        Output

        5 Years 11 Months
        """

        if end_date == "Present":

            end = self.today

        else:

            end = datetime.strptime(

                end_date,

                "%Y-%m"

            )

        start = datetime.strptime(

            start_date,

            "%Y-%m"

        )

        months = (

            (end.year - start.year) * 12 +

            end.month -

            start.month

        )

        years = months // 12

        remaining_months = months % 12

        return {

            "years": years,

            "months": remaining_months,

            "total_months": months

        }