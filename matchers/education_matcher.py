import re


class EducationMatcher:

    def __init__(self):

        self.levels = {
            "high school": 1,
            "associate": 2,
            "bachelor": 3,
            "master": 4,
            "phd": 5
        }

    def extract_degree(self, text):

        text = (text or "").lower()

        if re.search(r"\bph\.?d\b|\bdoctor\b", text):
            return "phd"

        if re.search(r"\bmaster\b|\bm\.?sc\b|\bmsc\b|\bms\b", text):
            return "master"

        if re.search(r"\bbachelor\b|\bb\.?sc\b|\bbsc\b|\bb\.?tech\b|\bbeng\b|\bb\.?eng\b", text):
            return "bachelor"

        if re.search(r"\bassociate\b", text):
            return "associate"

        if re.search(r"\bhigh school\b", text):
            return "high school"

        return None

    def match(self, cv, job):

        required = self.extract_degree(
            getattr(job, "required_education", "")
        )

        candidate = self.extract_degree(
            cv.sections.get("education", "")
        )

        if required is None:
            return {
                "matched": True,
                "required": None,
                "candidate": candidate
            }

        if candidate is None:
            return {
                "matched": False,
                "required": required,
                "candidate": None
            }

        return {
            "matched": self.levels[candidate] >= self.levels[required],
            "required": required,
            "candidate": candidate
        }