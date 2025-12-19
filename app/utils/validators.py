def validate_sql(sql: str):
    if not sql.lower().strip().startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")
