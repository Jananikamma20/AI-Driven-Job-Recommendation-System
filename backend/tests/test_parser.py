from backend.resume_parser.parser import ResumeParser

# Create parser object
parser = ResumeParser()

# Path to your resume
resume_path = r"Data/Resumes/resume_pdfs/resume.pdf"   # Change this path

# Parse the resume
result = parser.parse(resume_path)

# Print the result
print(result)