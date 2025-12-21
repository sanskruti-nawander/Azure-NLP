# app/config/db_config.py

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

password = quote_plus(os.getenv("DB_PASSWORD"))

DB_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{password}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(
    DB_URL,
    connect_args={"sslmode": os.getenv("DB_SSLMODE", "require")}
)
