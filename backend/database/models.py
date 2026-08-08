from backend.database.database import get_connection


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    # -------------------------
    # Users
    # -------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # -------------------------
    # Resumes
    # -------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            file_name TEXT,

            resume_data TEXT NOT NULL,

            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id)

                REFERENCES users(id)

                ON DELETE SET NULL

        )
    """)

    # -------------------------
    # Jobs
    # -------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            company TEXT,

            job_data TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    # -------------------------
    # Recommendations
    # -------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_id INTEGER,

            job_id INTEGER,

            overall_match REAL,

            ats_score REAL,

            recommendation TEXT,

            recommendation_data TEXT NOT NULL,

            generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (resume_id)

                REFERENCES resumes(id)

                ON DELETE CASCADE,

            FOREIGN KEY (job_id)

                REFERENCES jobs(id)

                ON DELETE CASCADE

        )
    """)

    connection.commit()

    connection.close()