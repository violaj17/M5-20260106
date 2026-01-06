# WIP

import pandas as pd
from sqlalchemy import create_engine

# 1. Create engine
connection_string = (
    "mssql+pyodbc://@SERVER_NAME/DATABASE_NAME"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load csv into DataFrame
book_df = pd.read_csv("./Cleaned data/03_Library Systembook_cleaned.csv")

# 2. Write DataFrame to SQL Server
book_df.to_sql(
    "CleanBooks",
    con=engine,
    if_exists="replace",
    index=False
)


