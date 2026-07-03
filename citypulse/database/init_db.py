from citypulse.database.connection import get_connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        report_id TEXT PRIMARY KEY,
        raw_text TEXT NOT NULL,
        image_url TEXT,
        latitude REAL,
        longitude REAL,
        ward TEXT,
        created_at TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS triage_results (
        report_id TEXT PRIMARY KEY,
        category TEXT NOT NULL,
        severity TEXT NOT NULL,
        confidence REAL,
        rationale TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()