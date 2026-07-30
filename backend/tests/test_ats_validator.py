from backend.ats_engine.ats_validator import ATSValidator

validator = ATSValidator()

print(validator.validate(-15))

print(validator.validate(78.567))

print(validator.validate(120))