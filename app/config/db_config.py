import os
import socket
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pathlib import Path

# Force IPv4 (CRITICAL FIX)
orig_getaddrinfo = socket.getaddrinfo
def ipv4_only_getaddrinfo(*args, **kwargs):
    return [addr for addr in orig_getaddrinfo(*args, **kwargs) if addr[0] == socket.AF_INET]
socket.getaddrinfo = ipv4_only_getaddrinfo

load_dotenv(dotenv_path=Path(".env"))

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DB_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DB_URL,
    connect_args={"sslmode": "require"}
)
