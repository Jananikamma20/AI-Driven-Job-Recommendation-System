from backend.certification_engine.certification_detector import CertificationDetector

from backend.certification_engine.certification_validator import CertificationValidator


class CertificationEngine:

    def __init__(self):

        self.detector = CertificationDetector()

        self.validator = CertificationValidator()


    def extract(self, resume_text):

        detected = self.detector.extract(

            resume_text

        )

        valid, invalid = self.validator.validate(

            detected

        )

        return {

            "certifications": valid,

            "invalid_certifications": invalid

        }