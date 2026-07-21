import re
from knowledge.skills import SKILL_MAP


class EvidenceExtractor:

    def extract(self, cv, keywords):

        evidence = {}

        for keyword in keywords:

            evidence[keyword] = []

            # Eğer bilgi tabanında varsa tüm eş anlamlıları al,
            # yoksa sadece kendisini ara.
            aliases = SKILL_MAP.get(keyword, [keyword])

            for section_name, section_text in cv.sections.items():

                found = False

                for alias in aliases:

                    pattern = re.compile(
                        r"\b" + re.escape(alias) + r"\b",
                        re.IGNORECASE
                    )

                    if pattern.search(section_text):

                        evidence[keyword].append(
                            {
                                "section": section_name,
                                "matched": alias,
                                "text": section_text.strip()
                            }
                        )

                        found = True
                        break

                # Aynı section'ı iki kere eklememek için
                if found:
                    continue

        return evidence