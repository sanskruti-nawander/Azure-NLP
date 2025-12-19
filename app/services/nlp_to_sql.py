from app.config.azure_config import client, DEPLOYMENT_NAME

SCHEMA_CONTEXT = """
You are querying a PostgreSQL database.

Table: customers
Columns:
- realid (TEXT)
- reporting_month (DATE)
- firstname (TEXT)
- lastname (TEXT)
- principal_os (NUMERIC)
- bucket_new (TEXT)
- plan_eligibility (BOOLEAN)
- payment_status (TEXT)

Table: call_logs
Columns:
- call_id (UUID)
- realid (TEXT)
- attempt_date (DATE)
- call_success (BOOLEAN)
- ptp_captured (BOOLEAN)
- ptp_amount (NUMERIC)
"""


SYSTEM_PROMPT = """
You are an expert PostgreSQL SQL generator.

Rules:
- Generate ONLY valid PostgreSQL SELECT queries.
- Do NOT use markdown or code blocks.
- Use TRUE/FALSE for boolean columns.
- For text comparisons, use case-insensitive matching (ILIKE).
- Use only the provided schema.
- Do not add explanations or comments.
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
