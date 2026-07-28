from backend.recommendation_engine.recommendation_validator import RecommendationValidator

validator = RecommendationValidator()

recommendations = [

    {

        "score": 3,

        "job": {

            "title": "Data Scientist"

        }

    },

    {

        "score": 0,

        "job": {

            "title": "Restaurant Manager"

        }

    }

]

valid, invalid = validator.validate(

    recommendations

)

print("\nVALID JOBS\n")

for job in valid:

    print(job)

print("\nINVALID JOBS\n")

for job in invalid:

    print(job)