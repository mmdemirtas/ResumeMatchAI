from pypdf import PdfReader


class PdfParser:
    def read(self,file):

        try:

            reader = PdfReader(file)  ## Pdf i açar.
            text = ""

            for page in reader.pages:  ## reader.pages pdf teki her sayfayı temsil ediyor. yani for döngüsüyle her sayfada tek tek dolaşıyoruz.

              text += page.extract_text() or ""##pdf teki yazıları tek bir string halinde çıkarıyor.or""yazdık.eğerilkfonksiyon none sonucuverirseonunyerineboşlukgelecek
            
            return text
        except Exception:
            return ""
