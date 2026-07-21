from resume_engine import ResumeEngine
from matchers.resume_matcher import ResumeMatcher
from extractors.evidence_extractor import EvidenceExtractor

from ResumeMatchAI.semantic_matcher import SemanticMatcher
from extractors.sentence_extractor import SentenceExtractor
from search.semantic_search import SemanticSearch

engine = ResumeEngine()

cvs = engine.load_cvs("sample_cv")

job = engine.load_job(
    "job_description/python_backend.txt"
)

matcher = ResumeMatcher()

ranking = matcher.match_all(cvs, job)

print("\nRANKING")
print("=" * 60)

for i, candidate in enumerate(ranking, start=1):

    print(f"{i}. {candidate['candidate']}")
    print(f"Score   : {candidate['score']}%")
    print(f"Matched : {candidate['matched']} / {candidate['total']}")
    print("-" * 60)


