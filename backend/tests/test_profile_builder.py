from backend.candidate_profile.profile_builder import ProfileBuilder

builder = ProfileBuilder()

profile = builder.build(

    {"companies":["Microsoft"]},

    {"normalized_skills":["Python","SQL"]},

    {"normalized_degrees":["Bachelor of Technology"]},

    {"projects":["AI Job Recommendation System"]},

    {"certifications":["NPTEL"]}

)

print(profile)