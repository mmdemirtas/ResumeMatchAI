import re


class RequirementExtractor:

    SKILL_IGNORE = [

        "degree",
        "years",
        "year",
        "experience"

    ]


    def extract(self, job):

        skills = []

        education = ""

        experience = ""

        if "requirements" not in job.sections:

            return skills, education, experience

        text = job.sections["requirements"]

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if "degree" in lower:

                education = line
                continue

            if "year" in lower and "experience" in lower:

                experience = line
                continue

            skills.append(line)

        return skills, education, experience