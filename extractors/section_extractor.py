class SectionExtractor:

    def __init__(self):

        self.headers = {

            # Summary
            "summary": "summary",
            "professional summary": "summary",
            "profile": "summary",
            "about": "summary",

            # Education
            "education": "education",
            "academic background": "education",

            # Experience
            "experience": "experience",
            "work experience": "experience",
            "employment history": "experience",
            "professional experience": "experience",

            # Projects
            "projects": "projects",
            "project experience": "projects",

            # Skills
            "skills": "skills",
            "technical skills": "skills",
            "core skills": "skills",

            # Languages
            "language": "languages",
            "languages": "languages",

            # Certificates
            "certificate": "certificates",
            "certificates": "certificates",
            "certifications": "certificates",

            # Leadership
            "leadership": "leadership",
            "leadership & activities": "leadership",
            "activities": "leadership"
        }

    def extract(self, text):

        lines = text.splitlines()

        sections = {}

        current_section = None

        for line in lines:

            line = line.strip()

            if not line:
                continue

            header = line.lower()

            matched = False

            for key, value in self.headers.items():

                # Başlığın içinde anahtar kelime geçiyor mu?
                if key in header:

                    current_section = value

                    if current_section not in sections:
                        sections[current_section] = ""

                    matched = True
                    break

            if matched:
                continue

            if current_section:
                sections[current_section] += line + "\n"

        # Sondaki gereksiz boşlukları temizle
        for section in sections:
            sections[section] = sections[section].strip()

        return sections
        
