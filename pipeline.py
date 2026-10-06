import os

import pandas as pd
from sqlalchemy import create_engine


# Extract
sales_data = pd.read_csv("data/sales.csv")

# Transform
sales_data["total_amount"] = (
    sales_data["quantity"] * sales_data["price"]
)

print("Transformed data:")
print(sales_data)


# Database configuration
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")


# Load
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}"
    f"@{db_host}:{db_port}/{db_name}"
)

sales_data.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False,
)

print("Data loaded successfully into PostgreSQL!")