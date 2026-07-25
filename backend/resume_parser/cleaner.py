import re


class ResumeCleaner:

    def __init__(self):
        pass


    def clean(self, text):

        if not text:
            return ""

        # Convert to lowercase
        text = text.lower()

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove unwanted characters
        text = re.sub(
            r"[^a-z0-9\s@.+#/-]",
            " ",
            text
        )

        # Remove multiple spaces
        text = re.sub(
            r"\s+",
            " ",
            text
        )

        # Remove leading and trailing spaces
        text = text.strip()

        return text