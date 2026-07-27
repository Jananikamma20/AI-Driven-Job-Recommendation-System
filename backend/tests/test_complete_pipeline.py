from backend.pipeline.resume_pipeline import ResumePipeline

pipeline = ResumePipeline()

resume_path = "Data/Resumes/resume_pdfs/resume.pdf"

result = pipeline.process_resume(resume_path)

print("=" * 60)
print("EXPERIENCE")
print("=" * 60)
print(result["experience"])

print("\n")

print("=" * 60)
print("SKILLS")
print("=" * 60)
print(result["skills"])

print("\n")

print("=" * 60)
print("EDUCATION")
print("=" * 60)
print(result["education"])