import re


class SentenceExtractor:

    def extract(self, sections):

        sentences = []

        for section_name, section_text in sections.items():

            lines = section_text.split("\n")

            for line in lines:

                line = line.strip()

                if len(line) < 3:
                    continue

                sentences.append(
                    {
                        "section": section_name,
                        "text": line
                    }
                )

        return sentences