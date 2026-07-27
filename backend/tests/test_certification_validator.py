from backend.certification_engine.certification_validator import CertificationValidator

validator = CertificationValidator()

certifications = [

    "AWS",

    "AI",

    "",

    "Google Data Analytics"

]

valid, invalid = validator.validate(

    certifications

)

print("\nValid Certifications\n")

for certification in valid:

    print(certification)

print("\nInvalid Certifications\n")

for certification in invalid:

    print(certification)