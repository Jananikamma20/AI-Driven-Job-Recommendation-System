from backend.education_engine.degree_normalizer import DegreeNormalizer

normalizer = DegreeNormalizer()

degrees = [

    "B.Tech",
    "B Tech",
    "BE",
    "B.E",
    "MBA",
    "M.Sc",
    "MSc",
    "PhD"

]

result = normalizer.normalize(degrees)

print("\nNormalized Degrees\n")

for degree in result:

    print(degree)