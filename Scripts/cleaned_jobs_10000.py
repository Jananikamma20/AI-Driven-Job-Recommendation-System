import pandas as pd
import re

def clean_job_summary(text):

    # Remove HTML tags
    text = re.sub(r'<.*?>', ' ', text)

    # Remove URLs
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'www\S+', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# Load Dataset
df = pd.read_csv("Data/Jobs/jobs_10000.csv")

print("=" * 50)
print("Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)

df = df.drop_duplicates()

print("\nAfter removing duplicates")
print(df.shape)

df = df.dropna()

print("\nAfter removing null values")
print(df.shape)

df["job_summary"] = df["job_summary"].apply(clean_job_summary)

df.to_csv(
    "Data/Jobs/cleaned_jobs_10000.csv",
    index=False
)

print("Job dataset cleaned successfully.")