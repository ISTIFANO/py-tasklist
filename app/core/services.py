import sys
import os
from sqlalchemy import select,delete,values,update
from models import tasks_table

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from infra.database import connection_to_db

db = connection_to_db()

def execution(stmt):
    with db.begin() as conn: 
      result = conn.execute(stmt).mappings()
    for row in result:
          print(row) 

def fetchAll():
    resultat = execution(select(tasks_table))
    return resultat
def Delete(id):
    resultat = execution(delete(tasks_table).where(tasks_table.c.id == id))
    print("data deleted succ")
    return resultat
def insert(contenu , priorite="LOW",status="TODO"):
        resultat = execution(insert(tasks_table).values(contenu=contenu,priorite=priorite,status=status ))
        print("data created succ")
        return resultat
def findbyId(id):
     resultat = select(tasks_table).where(tasks_table.c.id == id)
     return resultat
def updateValues(id, contenu, priorite, status):
    stmt = (
        update(tasks_table)
        .where(tasks_table.c.id == id)
        .values(contenu=contenu, priorite=priorite, status=status)
    )
    resultat = execution(stmt)
    print("Data updated succ")
    return resultat

