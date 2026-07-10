import re


class CompanyDetector:

    def __init__(self):

        # Version 1
        # Later this will come from companies.csv

        self.company_names = [

            "Google",
            "Microsoft",
            "Amazon",
            "Apple",
            "Meta",

            "Infosys",
            "TCS",
            "Wipro",
            "Accenture",
            "Capgemini",
            "Cognizant",
            "IBM",
            "HCL",

            "Oracle",
            "Adobe",
            "Salesforce",

            "Deloitte",
            "EY",
            "PwC",
            "KPMG",

            "JPMorgan",
            "Goldman Sachs",

            "Intel",
            "NVIDIA",

            "Tesla",

            "Samsung"

        ]


    def extract(self, resume_text):

        companies = []

        for company in self.company_names:

            pattern = r"\b" + re.escape(company) + r"\b"

            if re.search(

                pattern,

                resume_text,

                re.IGNORECASE

            ):

                companies.append(company)

        companies = sorted(

            list(

                set(companies)

            )

        )

        return companies