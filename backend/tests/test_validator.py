from backend.experience_engine.validator import ExperienceValidator

validator = ExperienceValidator()

records = [

    {
        "company": "Microsoft",
        "designation": "Software Engineer",
        "start_date": "2018-01",
        "end_date": "2020-07",
        "experience": {
            "years": 2,
            "months": 6,
            "total_months": 30
        }
    },

    {
        "company": "Google",
        "designation": None,
        "start_date": "2021-01",
        "end_date": "Present",
        "experience": {
            "years": 4,
            "months": 0,
            "total_months": 48
        }
    }

]

valid, invalid = validator.validate(records)

print("\nValid Records\n")
print(valid)

print("\nInvalid Records\n")
print(invalid)