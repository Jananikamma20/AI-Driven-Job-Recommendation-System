from backend.experience_engine.date_normalizer import DateNormalizer

normalizer = DateNormalizer()

samples = [

    "08/2020",

    "08-2021",

    "08.2022",

    "Aug 2020",

    "August 2021",

    "2023",

    "Present",

    "Current",

    "Random Text"

]

for sample in samples:

    print(sample, " ---> ", normalizer.normalize(sample))