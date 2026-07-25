import os

from backend.resume_parser.pdf_parser import PDFParser
from backend.resume_parser.docx_parser import DOCXParser
from backend.resume_parser.cleaner import ResumeCleaner


class ResumeParser:

    def __init__(self):

        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.cleaner = ResumeCleaner()


    def parse(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":

            text = self.pdf_parser.extract_text(file_path)

        elif extension == ".docx":

            text = self.docx_parser.extract_text(file_path)

        else:

            raise ValueError(

                "Unsupported file format."

            )

        cleaned_text = self.cleaner.clean(text)

        return cleaned_text