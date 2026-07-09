import re
from datetime import datetime


class DateNormalizer:

    def __init__(self):

        # Month Mapping Dictionary

        self.months = {

            "jan": "01",
            "january": "01",

            "feb": "02",
            "february": "02",

            "mar": "03",
            "march": "03",

            "apr": "04",
            "april": "04",

            "may": "05",

            "jun": "06",
            "june": "06",

            "jul": "07",
            "july": "07",

            "aug": "08",
            "august": "08",

            "sep": "09",
            "sept": "09",
            "september": "09",

            "oct": "10",
            "october": "10",

            "nov": "11",
            "november": "11",

            "dec": "12",
            "december": "12"

        }

    #######################################################

    def normalize(self, date_text):

        if not date_text:

            return None

        date_text = date_text.strip()

        lower = date_text.lower()

        # -----------------------------
        # Present / Current
        # -----------------------------

        if lower in ["present", "current", "till date", "ongoing"]:

            return "Present"

        # -----------------------------
        # MM/YYYY
        # -----------------------------

        match = re.fullmatch(r"(\d{2})[\/\-.](\d{4})", date_text)

        if match:

            month = match.group(1)

            year = match.group(2)

            return f"{year}-{month}"

        # -----------------------------
        # Month YYYY
        # -----------------------------

        match = re.fullmatch(

            r"([A-Za-z]+)\s+(\d{4})",

            date_text

        )

        if match:

            month_name = match.group(1).lower()

            year = match.group(2)

            if month_name in self.months:

                month = self.months[month_name]

                return f"{year}-{month}"

        # -----------------------------
        # Year Only
        # -----------------------------

        match = re.fullmatch(

            r"\d{4}",

            date_text

        )

        if match:

            return date_text

        # -----------------------------
        # Unknown Format
        # -----------------------------

        return None