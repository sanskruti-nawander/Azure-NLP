import uuid
import json
from decimal import Decimal
from datetime import date, datetime
from sqlalchemy import text
from app.config.db_config import engine


def serialize_value(value):
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value


def log_query(question, sql, status, error=None):
    query_id = str(uuid.uuid4())
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO query_logs 
                VALUES (:id, :q, :s, :st, :e, now())
            """),
            {"id": query_id, "q": question, "s": sql, "st": status, "e": error}
        )
    return query_id

def log_result(query_id, result):
    # Make result JSON serializable
    safe_result = [
        {k: serialize_value(v) for k, v in row.items()}
        for row in result
    ]

    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO query_results 
                VALUES (:id, :qid, :res, :cnt, now())
            """),
            {
                "id": str(uuid.uuid4()),
                "qid": query_id,
                "res": json.dumps(safe_result),
                "cnt": len(safe_result)
            }
        )

