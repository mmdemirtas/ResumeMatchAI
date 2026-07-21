from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class SemanticMatcher:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def similarity(self, text1, text2):

        emb1 = self.model.encode(text1, convert_to_tensor=True)
        emb2 = self.model.encode(text2, convert_to_tensor=True)

        score = cos_sim(emb1, emb2)

        return float(score)

    def is_match(self, requirement, text, threshold=0.75):

        score = self.similarity(requirement, text)

        return score >= threshold, score
    
    def find_match(self, requirement, sections, threshold=0.75):

      best_score = 0
      best_section = None
      best_text = None

      for section_name, section_text in sections.items():

        score = self.similarity(
            requirement,
            section_text
        )

        if score > best_score:

            best_score = score
            best_section = section_name
            best_text = section_text

      if best_score >= threshold:

        return {
            "matched": True,
            "score": best_score,
            "section": best_section,
            "text": best_text
        }

      return {
        "matched": False,
        "score": best_score
      }