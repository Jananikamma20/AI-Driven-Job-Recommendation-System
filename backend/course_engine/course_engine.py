import pandas as pd


class CourseEngine:

    def __init__(self):

        self.courses_df = pd.read_csv(
            "Data/KnowledgeBase/Courses/courses.csv"
        )

        # Clean column values once when loading
        self.courses_df["skill_name"] = (
            self.courses_df["skill_name"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.lower()
        )

    # =====================================================
    # RECOMMEND COURSES FOR MISSING SKILLS
    # =====================================================

    def recommend_courses(self, missing_skills):

        if not missing_skills:

            return []

        recommended_courses = []

        for skill in missing_skills:

            if not skill:
                continue

            skill_clean = (
                str(skill)
                .strip()
                .lower()
            )

            matches = self.courses_df[
                self.courses_df["skill_name"]
                == skill_clean
            ]

            for _, row in matches.iterrows():

                recommended_courses.append({

                    "skill": skill,

                    "course_name":
                        row["course_name"],

                    "provider":
                        row["provider"],

                    "level":
                        row["level"]

                })

        return recommended_courses