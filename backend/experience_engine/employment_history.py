class EmploymentHistory:

    def __init__(self):

        pass


    def build(

            self,

            companies,

            designations,

            start_dates,

            end_dates,

            experiences

    ):

        employment_records = []

        total_records = min(

            len(companies),

            len(designations),

            len(start_dates),

            len(end_dates),

            len(experiences)

        )

        for i in range(total_records):

            record = {

                "company":

                    companies[i],

                "designation":

                    designations[i],

                "start_date":

                    start_dates[i],

                "end_date":

                    end_dates[i],

                "experience":

                    experiences[i]

            }

            employment_records.append(

                record

            )

        return employment_records