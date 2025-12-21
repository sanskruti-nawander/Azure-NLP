from app.config.azure_config import client, DEPLOYMENT_NAME

SCHEMA_CONTEXT = SCHEMA_CONTEXT = """
You are querying a PostgreSQL database hosted on Supabase.

Tables and columns:

customers:
- realid (text, primary key)
- name (text)
- phone (text)
- total_due (numeric)
- min_due (numeric)
- emi_avail (boolean)
- emi_interested (boolean)
- total_attempts (numeric)
- ptp_flagged (boolean)
- rtp_flagged (boolean)
- dispute_flagged (boolean)
- dispute_description (text)
- customer_sentiment (text)
- default_segment (text)
- payment_status (text) -- values like 'unpaid', 'paid'
- next_best_action (text)
- risk_segement (text)
- call_connected (boolean)
- call_successful (boolean)
- campaign_id (text)
- gender (text)
- bank (text)
- escalation (boolean)
- channel (text)
- state (text)
- city (text)
- pincode (text)
- rewards_amt (numeric)
- cust_del_segment (text)
- utilization (numeric)
- days_since_bill (numeric)
- enr_teams (text)
- enr_band (text)
- created_at (timestamp)
- updated_at (timestamp)

call_logs:
- call_id (uuid, primary key)
- realid (text, foreign key → customers.realid)
- assistant_id (text)
- platform (text)
- recording_url (text)
- call_cost (numeric)
- call_success (boolean)
- call_end_reason (text)
- call_duration (interval)
- attempt_date (date)
- attempt_time (time)
- attempt_number (numeric)
- call_transcript (text)
- call_summary (text)
- extracted (text)
- ptp_captured (boolean)
- ptp_amount (text)
- ptp_date (text)
- rtp_flagged (boolean)
- emi_interested (boolean)
- dispute_flagged (boolean)
- waiver_interested (boolean)
- escalation (boolean)
- customer_sentiment (text)
- agent_malfunctioning (text)
- next_best_action (text)

Rules:
- Generate ONLY valid PostgreSQL SELECT queries
- Use JOIN between customers and call_logs via realid when needed
- Use TRUE/FALSE for boolean fields
- Use ILIKE for text comparisons
- Do not modify or delete data
- Do not hallucinate tables or columns
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
