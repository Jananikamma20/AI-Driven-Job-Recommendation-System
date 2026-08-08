import json

from backend.database.database import get_connection


# ==========================================
# USER OPERATIONS
# ==========================================

def insert_user(name, email):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users (name, email)
        VALUES (?, ?)
        """,
        (name, email)
    )

    connection.commit()

    user_id = cursor.lastrowid

    connection.close()

    return user_id


def get_user(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    connection.close()

    if user:

        return dict(user)

    return None


# ==========================================
# RESUME OPERATIONS
# ==========================================

def insert_resume(

        user_id,

        file_name,

        resume_data

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO resumes (

            user_id,

            file_name,

            resume_data

        )

        VALUES (?, ?, ?)
        """,
        (
            user_id,

            file_name,

            json.dumps(resume_data)

        )
    )

    connection.commit()

    resume_id = cursor.lastrowid

    connection.close()

    return resume_id


def get_resume(resume_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM resumes
        WHERE id = ?
        """,
        (resume_id,)
    )

    resume = cursor.fetchone()

    connection.close()

    if resume:

        result = dict(resume)

        result["resume_data"] = json.loads(
            result["resume_data"]
        )

        return result

    return None


# ==========================================
# JOB OPERATIONS
# ==========================================

def insert_job(

        title,

        company,

        job_data

):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO jobs (

            title,

            company,

            job_data

        )

        VALUES (?, ?, ?)
        """,
        (
            title,

            company,

            json.dumps(job_data)

        )
    )

    connection.commit()

    job_id = cursor.lastrowid

    connection.close()

    return job_id


def get_job(job_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM jobs
        WHERE id = ?
        """,
        (job_id,)
    )

    job = cursor.fetchone()

    connection.close()

    if job:

        result = dict(job)

        result["job_data"] = json.loads(
            result["job_data"]
        )

        return result

    return None


# ==========================================
# RECOMMENDATION OPERATIONS
# ==========================================

def insert_recommendation(

        resume_id,

        job_id,

        recommendation_data

):

    connection = get_connection()

    cursor = connection.cursor()

    summary = recommendation_data.get(
        "summary",
        {}
    )

    cursor.execute(
        """
        INSERT INTO recommendations (

            resume_id,

            job_id,

            overall_match,

            ats_score,

            recommendation,

            recommendation_data

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            resume_id,

            job_id,

            summary.get(
                "overall_match",
                0
            ),

            summary.get(
                "ats_score",
                0
            ),

            summary.get(
                "recommendation",
                ""
            ),

            json.dumps(
                recommendation_data
            )

        )
    )

    connection.commit()

    recommendation_id = cursor.lastrowid

    connection.close()

    return recommendation_id


def get_recommendation(
        recommendation_id
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM recommendations
        WHERE id = ?
        """,
        (recommendation_id,)
    )

    recommendation = cursor.fetchone()

    connection.close()

    if recommendation:

        result = dict(
            recommendation
        )

        result["recommendation_data"] = json.loads(
            result["recommendation_data"]
        )

        return result

    return None


# ==========================================
# HISTORY
# ==========================================

def get_recommendation_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM recommendations
        ORDER BY generated_at DESC
        """
    )

    recommendations = cursor.fetchall()

    connection.close()

    return [
        dict(item)
        for item in recommendations
    ]