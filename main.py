from resume_engine import ResumeEngine
from matchers.resume_matcher import ResumeMatcher


engine = ResumeEngine()

# CV yükle
cv = engine.load_cv(
    "sample_cv/ZiyaKutayKatlandurCV.docx"
)

# İş ilanını yükle
job = engine.load_job(
    "job_description/python_backend.txt"
)

# Eşleştir
matcher = ResumeMatcher()

result = matcher.match(cv, job)

print("=" * 60)
print("RESUME MATCH REPORT")
print("=" * 60)

print(f"\nOverall Match Score : %{result['score']}")
print(f"Matched Skills      : {result['matched']} / {result['total']}")

print("\n" + "=" * 60)

for skill, info in result["skills"].items():

    status = "✓" if info["found"] else "✗"

    print(f"\n{status} {skill}")

    if not info["found"]:
        continue

    for item in info["evidence"]:

        print(f"\n[{item['section'].upper()}]")

        print(item["text"])

        print("-" * 40)