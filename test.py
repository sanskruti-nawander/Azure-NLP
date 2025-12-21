from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres.caimrweszlegqgdlsbyq:Predixion%40123@aws-0-ap-south-1.pooler.supabase.com:5432/postgres",
    connect_args={"sslmode": "require"}
)

with engine.connect() as conn:
    print(conn.execute("select 1").fetchone())
