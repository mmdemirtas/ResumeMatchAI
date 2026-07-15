from docx import Document

class DocxParser:
    def read(self,file):

        
        try:

          doc = Document(file)  ## word dosyasını açar.

          text = ""

          for paragraph in doc.paragraphs:  ## dosyanın içini paragraflara böler [paragraf1,paragraf2 ... ], her paragrafı tek tek dolaşıyoruz.

            text += paragraph.text + "\n"  ## Bütün paragrafları tek string içinde birleştiriyoruz

          return text
        
        except Exception:
        
         return ""


    
    
