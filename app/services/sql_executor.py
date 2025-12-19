from sqlalchemy import text
from app.config.db_config import engine
from app.utils.validators import validate_sql

def execute_sql(sql: str):
    cleaned_sql = validate_sql(sql)
    with engine.connect() as conn:
        result = conn.execute(text(cleaned_sql))
        rows = [dict(row._mapping) for row in result]
    return rows
