from app.config.db_config import engine

with engine.connect() as conn:
    result = conn.execute("SELECT 1")
    print(result.fetchone())
