from extractors.evidence_extractor import EvidenceExtractor


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