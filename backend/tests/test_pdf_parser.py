from backend.resume_parser.pdf_parser import PDFParser

parser = PDFParser()

pdf_path = "Data/Resumes/resume_pdfs/ACCOUNTANT/10554236.pdf"
text = parser.extract_text(pdf_path)

print(text)