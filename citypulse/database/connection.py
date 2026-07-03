from pathlib import Path
import sqlite3

# Project Root/
BASE_DIR = Path(__file__).resolve().parents[2]

# Project Root/data/
DATA_DIR = BASE_DIR / "data"

# Create data folder if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Project Root/data/citypulse.db
DATABASE_PATH = DATA_DIR / "citypulse.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)

    # Allows us to access columns by name
    connection.row_factory = sqlite3.Row

    return connection