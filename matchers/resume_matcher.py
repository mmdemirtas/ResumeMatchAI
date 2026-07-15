from extractors.evidence_extractor import EvidenceExtractor
from pathlib import Path


class ResumeMatcher:

    def __init__(self):

        self.extractor = EvidenceExtractor()

    def match(self, cv, job):

        evidence = self.extractor.extract(
            cv,
            job.required_skills
        )

        report = {}

        matched = 0

        total = len(job.required_skills)

        for skill in job.required_skills:

            found = len(evidence[skill]) > 0

            if found:
                matched += 1

            report[skill] = {

                "found": found,

                "evidence": evidence[skill]

            }

        score = 0

        if total > 0:
            score = round((matched / total) * 100)

        return {

            "score": score,

            "matched": matched,

            "total": total,

            "skills": report

        }
    def load_cvs(self, folder):

      folder = Path(folder)

      cvs = []

      for file in folder.iterdir():

        if not file.is_file():
            continue

        if file.suffix.lower() not in [".pdf", ".docx", ".txt"]:
            continue

        try:

            cv = self.load_cv(file)

            cvs.append(cv)

        except Exception as e:

            print(f"{file.name} okunamadi : {e}")

      return cvs