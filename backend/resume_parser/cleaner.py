import re


class ResumeCleaner:

    def __init__(self):
        pass

    def clean(self, text):

        if not text:
            return ""

        text = text.lower()

        text = text.replace("\t", " ")

        text = re.sub(
            r"[^a-z0-9\n\s@.+#/-]",
            " ",
            text
        )

        # Remove extra spaces but keep new lines
        text = re.sub(
            r"[ ]+",
            " ",
            text
        )

        # Remove too many blank lines
        text = re.sub(
            r"\n+",
            "\n",
            text
        )

        text = text.strip()

        return text