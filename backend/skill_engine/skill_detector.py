import re


class SkillDetector:

    def __init__(self):

        pass

    def detect(self, text, skills):

        if not text:

            return []

        detected = []

        text = text.lower()

        for skill in skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):

                detected.append(skill)

        return sorted(
            list(set(detected))
        )