from backend.resume_parser.pdf_parser import PDFParser
from backend.resume_parser.cleaner import ResumeCleaner

pdf = PDFParser()

cleaner = ResumeCleaner()

pdf_path = "Data/Resumes/resume_pdfs/ACCOUNTANT/10554236.pdf"

raw_text = pdf.extract_text(pdf_path)

clean_text = cleaner.clean(raw_text)

print("\nRAW TEXT\n")
print(raw_text[:1000])

print("\n-----------------------------\n")

print("CLEAN TEXT\n")
print(clean_text[:1000])