from pathlib import Path
import os

PROJECT_DIR = Path(__file__).parent
REFERENCE_DB_NAME = "catalogtest.db"
REFERENCE_TEST_DATABASE_PATH = os.path.join(PROJECT_DIR, REFERENCE_DB_NAME)