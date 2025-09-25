import sys
import os
from sqlalchemy import select,delete,update
custom_path = r'C:\Users\aamir\Desktop\YC\Python\py-tasklist\app\core'
if custom_path not in sys.path:
    sys.path.append(custom_path)
from models import tasks_table

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from infra.database import connection_to_db
db = connection_to_db()

def execution(stmt):
    with db.begin() as conn: 
        result = conn.execute(stmt).mappings().all()  
    return result  

def fetchAll():
    resultat = execution(select(tasks_table))
    return resultat

def fetchInProgressTasks():
     resultat = execution(select(tasks_table).where(tasks_table.columns.status=="PENDING"))
     return resultat
def fetchDoneTasks():
     resultat = execution(select(tasks_table).where(tasks_table.columns.status=="DONE"))
     return resultat
def fetchTodoTasks():
     resultat = execution(select(tasks_table).where(tasks_table.columns.status=="TODO"))
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
