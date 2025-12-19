from app.config.azure_config import client, DEPLOYMENT_NAME

SCHEMA_CONTEXT = """
Tables:
customers(realid, reporting_month, firstname, lastname, principal_os, bucket_new, plan_eligibility, payment_status)
call_logs(call_id, realid, attempt_date, call_success, ptp_captured, ptp_amount)
"""

SYSTEM_PROMPT = """
You are an expert PostgreSQL SQL generator.
Generate ONLY valid PostgreSQL SELECT queries.
Do not explain anything.
"""

def generate_sql(user_question: str) -> str:
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": SCHEMA_CONTEXT},
            {"role": "user", "content": user_question}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
