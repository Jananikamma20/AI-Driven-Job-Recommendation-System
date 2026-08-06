from backend.certification_engine.certification_engine import CertificationEngine

engine = CertificationEngine()

resume = {

    "certifications": [

        "IBM Data Science",

        "NPTEL Java Programming",

        "AWS Cloud Practitioner"

    ]

}

job = {

    "certifications": [

        "IBM Data Science",

        "Microsoft Azure Fundamentals",

        "AWS Cloud Practitioner"

    ]

}

result = engine.analyze(

    resume,

    job

)

print("=" * 60)
print("CERTIFICATION ENGINE TEST")
print("=" * 60)

print()

print("Certification Match")
print(result["certification_match"])

print()

print("Matched Certifications")
print(result["matched_certifications"])

print()

print("Missing Certifications")
print(result["missing_certifications"])

print()

print("Certification Score")
print(result["certification_score"])