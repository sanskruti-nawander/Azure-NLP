import re

def clean_sql(sql: str) -> str:
    # Remove ```sql and ``` blocks
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()

def validate_sql(sql: str):
    cleaned_sql = clean_sql(sql)
    if not cleaned_sql.lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")
    return cleaned_sql
