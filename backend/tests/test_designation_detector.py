from backend.experience_engine.designation_detector import DesignationDetector

detector = DesignationDetector()

resume = """

Senior Software Engineer

Worked as Software Engineer

Promoted to Engineering Manager

Python Developer

"""

designations = detector.extract(

    resume

)

print()

print("Detected Designations")

print("----------------------")

for d in designations:

    print(d)