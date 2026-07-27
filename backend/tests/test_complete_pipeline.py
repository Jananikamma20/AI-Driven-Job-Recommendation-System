from backend.pipeline.resume_pipeline import ResumePipeline

pipeline = ResumePipeline()

resume_path = "Data/Resumes/resume_pdfs/resume.pdf"

result = pipeline.process_resume(resume_path)

print("=" * 60)
print("CLEANED RESUME")
print("=" * 60)
print(result["cleaned_text"][:1000])

print("\n")

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

print("\n")

print("=" * 60)
print("PROJECTS")
print("=" * 60)
print(result["projects"])

print("\n")

print("=" * 60)
print("CERTIFICATIONS")
print("=" * 60)
print(result["certifications"])

print("\n")

print("=" * 60)
print("CANDIDATE PROFILE")
print("=" * 60)

print(result["candidate_profile"])