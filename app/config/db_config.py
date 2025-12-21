from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

DB_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{DB_PASSWORD}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_NAME')}"
)

engine = create_engine(
    DB_URL,
    connect_args={"sslmode": "require"}
)
