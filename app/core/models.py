from sqlalchemy import Column, Integer, String, Table, MetaData,Enum

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