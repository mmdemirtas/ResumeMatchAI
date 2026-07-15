class TxtParser:

    def read(self, file):

        try:
            with open(file, "r", encoding="utf-8") as f:
                return f.read()

        except Exception:
            return ""