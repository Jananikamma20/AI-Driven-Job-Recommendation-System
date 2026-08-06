import pandas as pd
import re

import re

def clean_resume(text):

    text = re.sub(r'<.*?>', ' ', text)

    text = re.sub(r'http\S+', ' ', text)

    text = re.sub(r'www\S+', ' ', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# Load dataset
df = pd.read_csv("Data/Resumes/Resume.csv")

# Dataset information
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

print("\nCategories")
print(df["Category"].value_counts())


df = df.drop_duplicates()

print("After removing duplicates")
print(df.shape)

df = df.dropna()

print("After removing null values")
print(df.shape)

df["Resume_str"] = df["Resume_str"].apply(clean_resume)

df.to_csv(
    "Data/Resumes/cleaned_resume.csv",
    index=False
)

print("Resume dataset cleaned successfully.")