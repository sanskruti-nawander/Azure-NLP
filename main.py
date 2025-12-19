from app.services.nlp_to_sql import generate_sql
from app.services.sql_executor import execute_sql
from app.services.query_logger import log_query, log_result

def main():
    question = input("\nAsk your question: ")

    try:
        sql = generate_sql(question)
        print("\nGenerated SQL:\n", sql)

        query_id = log_query(question, sql, "SUCCESS")

        result = execute_sql(sql)
        log_result(query_id, result)

        print("\nQuery Result:")
        for row in result:
            print(row)

    except Exception as e:
        log_query(question, None, "FAILED", str(e))
        print("Error:", e)

if __name__ == "__main__":
    main()
