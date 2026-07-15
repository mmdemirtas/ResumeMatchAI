import re


class EvidenceExtractor:

    def extract(self, cv, keywords):

        evidence = {}

        for keyword in keywords:

            evidence[keyword] = []

            pattern = re.compile(
                r"\b" + re.escape(keyword) + r"\b",
                re.IGNORECASE
            )

            for section_name, section_text in cv.sections.items():

                if pattern.search(section_text):

                    evidence[keyword].append(
                        {
                            "section": section_name,
                            "text": section_text.strip()
                        }
                    )

        return evidence