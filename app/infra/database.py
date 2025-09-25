import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

def connection_to_db():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    connection_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    print(connection_str)
    try:
        engine = create_engine(connection_str)
        with engine.connect() as conn:
            pass
        return engine
    except Exception as err:
        print(f"{err}")
        return None

