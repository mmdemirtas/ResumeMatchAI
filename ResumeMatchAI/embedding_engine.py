from sentence_transformers import SentenceTransformer


class EmbeddingEngine:

    _model = None

    def __init__(self):

        if EmbeddingEngine._model is None:

            print("Loading embedding model...")

            EmbeddingEngine._model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        self.model = EmbeddingEngine._model

    def encode(self, text):

        return self.model.encode(
            text,
            convert_to_tensor=True
        )