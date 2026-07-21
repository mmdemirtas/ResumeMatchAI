from ResumeMatchAI.embedding_engine import EmbeddingEngine
from sentence_transformers.util import cos_sim


class SemanticSearch:

    def __init__(self):

        self.embedding = EmbeddingEngine()

    def search(self, query, cv, top_k=5):

        query_embedding = self.embedding.encode(query)

        results = []

        for item in cv.embeddings:

            score = float(
                cos_sim(
                    query_embedding,
                    item["embedding"]
                )
            )

            results.append(
                {
                    "score": score,
                    "section": item["section"],
                    "text": item["text"]
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results[:top_k]