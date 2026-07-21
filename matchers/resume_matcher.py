from search.semantic_search import SemanticSearch
from knowledge.requirement_expander import RequirementExpander
from matchers.education_matcher import EducationMatcher
from matchers.experience_matcher import ExperienceMatcher


class ResumeMatcher:

    def __init__(self):

        self.search = SemanticSearch()
        self.expander = RequirementExpander()
        self.education_matcher = EducationMatcher()
        self.experience_matcher = ExperienceMatcher()
        

    def match(self, cv, job):

        report = {}

        matched = 0

        total = len(job.required_skills)

        for skill in job.required_skills:

            expanded = self.expander.expand(skill)

            results = self.search.search(
                expanded,
                cv,
                top_k=3
            )

            best_score = results[0]["score"] if results else 0

            found = best_score >= 0.45

            if found:
                matched += 1
            
            print("\n")
            print("=" * 50)
            print(skill)
            print(f"Expanded : {expanded}")
            print(f"Best Score : {best_score:.3f}")

            if results:

              print(results[0]["text"])

              report[skill] = {
                "found": found,
                "score": round(best_score, 3),
                "evidence": results
              }
        education = self.education_matcher.match(
         cv,
         job
        )
        experience = self.experience_matcher.match(
         cv,
         job
        )

        score = 0

        if total > 0:
            score = round((matched / total) * 100)

        return {
            "score": score,
            "matched": matched,
            "total": total,
            "skills": report,
            "education": education,
            "experience": experience
        }

    def match_all(self, cvs, job):

        ranking = []

        for cv in cvs:

            result = self.match(cv, job)

            ranking.append({
                "candidate": cv.file_name,
                "score": result["score"],
                "matched": result["matched"],
                "total": result["total"],
                "details": result["skills"]
            })

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranking