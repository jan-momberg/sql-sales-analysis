from sqlalchemy import create_engine

DB_USER = "janmomberg"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "sql_portfolio"

def get_engine():
    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(connection_string)
