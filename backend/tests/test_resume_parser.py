from backend.resume_parser.parser import ResumeParser

parser = ResumeParser()

pdf_path = "Data/Resumes/resume_pdfs/ACCOUNTANT/10554236.pdf"

text = parser.parse(pdf_path)

print("\nPDF OUTPUT\n")

print(text[:1000])


docx_path = "Data/Resumes/sample_resume.docx"

text = parser.parse(docx_path)

print("\nDOCX OUTPUT\n")

print(text)