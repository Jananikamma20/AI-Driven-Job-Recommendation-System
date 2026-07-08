from backend.experience_engine.date_detector import DateDetector

resume = """
Software Engineer

January 2018 to March 2021

Senior Engineer

Aug 2021 to Present
"""

detector = DateDetector()

result = detector.detect_dates(resume)

print(result)