CREATE TABLE IF NOT EXISTS customers (
    realid VARCHAR(50),
    reporting_month DATE,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    principal_os NUMERIC(12,2),
    bucket_new VARCHAR(50),
    plan_eligibility BOOLEAN,
    payment_status VARCHAR(50),
    PRIMARY KEY (realid, reporting_month),
    UNIQUE (realid)     -- ✅ ADD THIS
);

CREATE TABLE IF NOT EXISTS call_logs (
    call_id UUID PRIMARY KEY,
    realid VARCHAR(50),
    attempt_date DATE,
    call_success BOOLEAN,
    ptp_captured BOOLEAN,
    ptp_amount NUMERIC(12,2),
    FOREIGN KEY (realid) REFERENCES customers(realid)
);

CREATE TABLE IF NOT EXISTS query_logs (
    query_id UUID PRIMARY KEY,
    user_question TEXT,
    generated_sql TEXT,
    execution_status VARCHAR(20),
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS query_results (
    result_id UUID PRIMARY KEY,
    query_id UUID,
    result_data JSONB,
    row_count INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
