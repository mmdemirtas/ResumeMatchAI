from pathlib import Path
from models.cv import CV
from models.job import Job

from parsers.txt_parser import TxtParser
from parsers.pdf_parser import PdfParser
from parsers.docx_parser import DocxParser
from extractors.section_extractor import SectionExtractor
from extractors.job_section_extractor import JobSectionExtractor
from extractors.requirement_extractor import RequirementExtractor


class ResumeEngine:
    def __init__(self):
        self.txt_parser = TxtParser()
        self.pdf_parser = PdfParser()
        self.docx_parser = DocxParser()
        self.section_extractor = SectionExtractor()
        self.job_section_extractor = JobSectionExtractor()
        self.requirement_extractor = RequirementExtractor()

    def load_cv(self,file_path):

        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(f"{file} bulunamadi.") 
        
        if file.suffix == ".txt":
            text = self.txt_parser.read(file)

        elif file.suffix == ".pdf":
            text = self.pdf_parser.read(file)

        elif file.suffix == ".docx":
            text = self.docx_parser.read(file)

        else:
            raise ValueError("Desteklenmeyen dosya formati.")

        cv = CV()

        cv.file_name = file.name
        cv.text = text

        cv.sections = self.section_extractor.extract(text)


        return cv
    
    def load_job(self, file):

      file = Path(file)

      if not file.exists():
        raise FileNotFoundError(f"{file} bulunamadi.")

      job = Job()

      job.file_name = file.name

      if file.suffix == ".txt":
        text = self.txt_parser.read(file)

      elif file.suffix == ".pdf":
        text = self.pdf_parser.read(file)

      elif file.suffix == ".docx":
        text = self.docx_parser.read(file)

      else:
        raise ValueError("Desteklenmeyen dosya.")

      job.text = text

      job.sections = self.job_section_extractor.extract(text)

      skills, education, experience = self.requirement_extractor.extract(job)

      job.required_skills = skills
      job.required_education = education
      job.required_experience = experience

      return job

        
    
