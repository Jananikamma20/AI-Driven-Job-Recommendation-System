import pandas as pd

# Load the jobs dataset
jobs_df = pd.read_csv("Data/Jobs/cleaned_jobs_10000.csv")

# Load the job skills dataset
skills_df = pd.read_csv("Data/Jobs/cleaned_job_skills.csv")

print("=" * 50)
print("Jobs Dataset Shape:", jobs_df.shape)
print("Job Skills Dataset Shape:", skills_df.shape)

# Get all job links from the jobs dataset
job_links = set(jobs_df["job_link"])

print("\nUnique Job Links:", len(job_links))

# Keep only the skills that belong to those jobs
filtered_skills = skills_df[
    skills_df["job_link"].isin(job_links)
]

print("\nFiltered Job Skills Shape:", filtered_skills.shape)

# Remove duplicate rows (just in case)
filtered_skills = filtered_skills.drop_duplicates()

print("After Removing Duplicates:", filtered_skills.shape)

# Save the filtered dataset
filtered_skills.to_csv(
    "Data/Jobs/filtered_job_skills.csv",
    index=False
)

print("\n✅ Filtered Job Skills dataset created successfully!")