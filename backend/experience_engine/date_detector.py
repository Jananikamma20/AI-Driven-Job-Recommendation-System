import re
from typing import Dict, List

from .patterns import DATE_PATTERNS


class DateDetector:
    
    def __init__(self):

        # Load all regex patterns
        self.patterns = DATE_PATTERNS

    def detect_dates(self, text: str) -> Dict[str, List[str]]:
        """
        Detect every supported date format.

        Parameters
        ----------
        text : str
            Resume text

        Returns
        -------
        Dict
            Dictionary containing all detected dates
        """

        detected_dates = {}

        for pattern_name, regex_pattern in self.patterns.items():

            matches = re.findall(
                regex_pattern,
                text,
                flags=re.IGNORECASE
            )

            cleaned_matches = []

            for match in matches:

                if isinstance(match, tuple):
                    value = " ".join(match)

                else:
                    value = match

                value = value.strip()

                if value not in cleaned_matches:
                    cleaned_matches.append(value)

            detected_dates[pattern_name] = cleaned_matches

        return detected_dates