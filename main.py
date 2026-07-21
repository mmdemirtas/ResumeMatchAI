from resume_engine import ResumeEngine
from matchers.resume_matcher import ResumeMatcher


def main():

    engine = ResumeEngine()

    matcher = ResumeMatcher()

    # Load all CVs
    cvs = engine.load_cvs("sample_cv")

    # Load Job Description
    job = engine.load_job(
        "job_description/python_backend.txt"
    )

    # Match all candidates
    ranking = matcher.match_all(cvs, job)

    print("\nRANKING")
    print("=" * 60)

    for i, candidate in enumerate(ranking, start=1):

        print(f"{i}. {candidate['candidate']}")
        print(f"Overall Score : {candidate['score']}%")
        print(f"Matched Skills: {candidate['matched']} / {candidate['total']}")

        print("-" * 60)

    # Detailed report for the best candidate

    if ranking:

        best_name = ranking[0]["candidate"]

        best_cv = next(
            cv for cv in cvs
            if cv.file_name == best_name
        )

        result = matcher.match(best_cv, job)

        print("\nBEST CANDIDATE")
        print("=" * 60)

        print(f"Candidate : {best_name}")

        print("\nSkill Analysis")

        for skill, info in result["skills"].items():

            status = "✓" if info["found"] else "✗"

            print(
                f"{status} {skill:15}"
                f" Score: {info['score']:.3f}"
            )

        print("\nEducation")
        print(
            f"Required : {result['education']['required']}"
        )
        print(
            f"Candidate: {result['education']['candidate']}"
        )
        print(
            f"Matched  : {result['education']['matched']}"
        )

        print("\nExperience")
        print(
            f"Required : {result['experience']['required']} years"
        )
        print(
            f"Candidate: {result['experience']['candidate']} years"
        )
        print(
            f"Matched  : {result['experience']['matched']}"
        )


if __name__ == "__main__":
    main()