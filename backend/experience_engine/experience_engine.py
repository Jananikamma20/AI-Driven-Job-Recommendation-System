from backend.experience_engine.date_detector import DateDetector
from backend.experience_engine.date_normalizer import DateNormalizer
from backend.experience_engine.experience_calculator import ExperienceCalculator
from backend.experience_engine.designation_detector import DesignationDetector
from backend.experience_engine.company_detector import CompanyDetector


class ExperienceEngine:

    def __init__(self):

        self.date_detector = DateDetector()
        self.date_normalizer = DateNormalizer()
        self.experience_calculator = ExperienceCalculator()
        self.designation_detector = DesignationDetector()
        self.company_detector = CompanyDetector()

    def extract(self, resume_text):

        # Detect all dates
        detected_dates = self.date_detector.detect_dates(resume_text)

        # Extract companies
        companies = self.company_detector.extract(resume_text)

        # Extract designations
        designations = self.designation_detector.extract(resume_text)

        # Store experience information
        experience_details = []

        # Supported date ranges
        range_keys = [
            "MONTH_YEAR_RANGE",
            "MONTH_PRESENT"
        ]

        for key in range_keys:

            for value in detected_dates.get(key, []):

                if " - " not in value:
                    continue

                start, end = value.split(" - ")

                start = self.date_normalizer.normalize(start.strip())
                end = self.date_normalizer.normalize(end.strip())

                if start is None or end is None:
                    continue

                experience = self.experience_calculator.calculate(
                    start,
                    end
                )

                experience_details.append({

                    "start_date": start,
                    "end_date": end,
                    "experience": experience

                })

        return {

            "companies": companies,

            "designations": designations,

            "date_ranges": experience_details

        }