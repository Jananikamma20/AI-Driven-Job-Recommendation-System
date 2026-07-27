from backend.candidate_profile.candidate_profile_engine import CandidateProfileEngine

engine = CandidateProfileEngine()

result = engine.build(

    {"companies":["Microsoft"]},

    {"normalized_skills":["Python","SQL"]},

    {"normalized_degrees":["Bachelor of Technology"]},

    {"projects":["AI Job Recommendation System"]},

    {"certifications":["NPTEL"]}

)

print(result)