from sqlalchemy import Column, Integer, String, Table, MetaData, Enum,insert
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.infra.database import connection_to_db

engine = connection_to_db()
metadata = MetaData()

status = Enum("TODO", "PENDING", "DONE", name="enum")
priorite = Enum("HIGH", "LOW", "MEDIUM", name="priorite_enum")


tasks_table = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("contenu", String, nullable=False),
    Column("status", status,default="TODO"),
    Column("priorite", priorite,default="LOW")
)
# metadata.create_all(engine)

stmt = insert(tasks_table).values(
    contenu="migration done ",
    status="DONE",
    priorite="LOW"
)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
