import re
from datetime import datetime


class ExperienceMatcher:

    def extract_required_years(self, text):

        text = text.lower()

        match = re.search(r"(\d+)\+?\s*years?", text)

        if match:
            return int(match.group(1))

        return 0

    def calculate_experience(self, text):

        current = datetime.now().year

        years = re.findall(
            r"(20\d{2})\s*[-–]\s*(20\d{2}|present)",
            text.lower()
        )

        total = 0

        for start, end in years:

            start = int(start)

            if end == "present":
                end = current
            else:
                end = int(end)

            total += max(0, end - start)

        return total

    def match(self, cv, job):

        required = self.extract_required_years(
            job.required_experience
        )

        experience_text = cv.sections.get(
            "experience",
            ""
        )

        candidate = self.calculate_experience(
            experience_text
        )

        return {

            "required": required,

            "candidate": candidate,

            "matched": candidate >= required

        }