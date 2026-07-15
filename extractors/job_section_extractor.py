import re


class JobSectionExtractor:

    HEADINGS = [

        "requirements",
        "responsibilities",
        "qualifications",
        "preferred qualifications",
        "preferred skills",
        "benefits",
        "about us",
        "about the company",
        "what you'll do",
        "what you will do",
        "what we offer",
        "who you are",
        "skills",
        "experience",
        "education"

    ]

    def extract(self, text):

        sections = {}

        current = "general"

        sections[current] = ""

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            if lower in self.HEADINGS:

                current = lower
                sections[current] = ""

            else:

                sections[current] += line + "\n"

        return sections