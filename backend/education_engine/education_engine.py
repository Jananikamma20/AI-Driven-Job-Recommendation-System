from backend.education_engine.education_detector import EducationDetector
from backend.education_engine.degree_normalizer import DegreeNormalizer


class EducationEngine:

    def __init__(self):

        self.detector = EducationDetector()

        self.normalizer = DegreeNormalizer()


    def extract(self, resume_text):

        detected_degrees = self.detector.extract(
            resume_text
        )

        normalized_degrees = self.normalizer.normalize(
            detected_degrees
        )

        return {

            "detected_degrees": detected_degrees,

            "normalized_degrees": normalized_degrees

        }