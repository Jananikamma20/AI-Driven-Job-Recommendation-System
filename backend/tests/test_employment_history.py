from backend.experience_engine.employment_history import EmploymentHistory

builder = EmploymentHistory()

companies = [

    "Infosys",

    "Microsoft"

]

designations = [

    "Software Engineer",

    "Senior Software Engineer"

]

start_dates = [

    "2018-07",

    "2020-08"

]

end_dates = [

    "2020-07",

    "Present"

]

experiences = [

    {

        "years":2,

        "months":0,

        "total_months":24

    },

    {

        "years":5,

        "months":11,

        "total_months":71

    }

]

records = builder.build(

    companies,

    designations,

    start_dates,

    end_dates,

    experiences

)

for record in records:

    print(record)