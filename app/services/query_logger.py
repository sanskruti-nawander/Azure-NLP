import uuid
import json
from sqlalchemy import text
from app.config.db_config import engine

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
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO query_results 
                VALUES (:id, :qid, :res, :cnt, now())
            """),
            {
                "id": str(uuid.uuid4()),
                "qid": query_id,
                "res": json.dumps(result),
                "cnt": len(result)
            }
        )
