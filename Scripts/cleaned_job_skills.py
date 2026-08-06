import pandas as pd
import re

def clean_job_skill(text):

    text = str(text)

    # Remove HTML tags (if any)
    text = re.sub(r'<.*?>', ' ', text)

    # Remove URLs (if any)
    text = re.sub(r'http\S+|www\S+', ' ', text)

    # Remove extra spaces only
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

df = pd.read_csv("Data/Jobs/job_skills.csv")

print("=" * 50)
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

df = df.drop_duplicates()

df = df.dropna(subset=["job_link", "job_skills"])

df["job_skills"] = df["job_skills"].apply(clean_job_skill)

print(df.head())

print(df.isnull().sum())

print(df.duplicated().sum())

df.to_csv(
    "Data/Jobs/cleaned_job_skills.csv",
    index=False
)

print("Job Skills dataset cleaned successfully.")