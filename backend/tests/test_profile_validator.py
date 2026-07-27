from backend.candidate_profile.profile_validator import ProfileValidator

validator = ProfileValidator()

profile = {

    "experience":{"companies":["Microsoft"]},

    "skills":{"normalized_skills":["Python"]},

    "education":{},

    "projects":{},

    "certifications":{"certifications":["NPTEL"]}

}

valid, invalid = validator.validate(profile)

print("\nVALID PROFILE\n")

print(valid)

print("\nINVALID PROFILE\n")

print(invalid)