import sys
import os
from sqlalchemy import select,delete,update,insert
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
def executionCrud(stmt):
    with db.begin() as conn: 
        result = conn.execute(stmt)
    return result  


def fetchAll():
    resultat = execution(select(tasks_table))
    return resultat
var = fetchAll()
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
    resultat = executionCrud(delete(tasks_table).where(tasks_table.c.id == id))
    print("data deleted succ")
    return resultat
def add_task(contenu, priorite="LOW", status="TODO"):
    stmt = insert(tasks_table).values(
        contenu=contenu,
        priorite=priorite,
        status=status
    )
    resultat = execution(stmt)
    print("data created successfully")
    return resultat

def find_by_id(id):
    stmt = select(tasks_table).where(tasks_table.c.id == id)
    result = execution(stmt)
    if result:               
        return result[0]      
    return None


def updatepriorite(id,priorite):
    stmt = (
        update(tasks_table)
        .where(tasks_table.c.id == id)
        .values( priorite=priorite)
    )
    resultat = executionCrud(stmt)
    print("Data updated succ")
    return resultat

def updatestatus(id,status):
    stmt = (
        update(tasks_table)
        .where(tasks_table.c.id == id)
        .values( status=status)
    )
    resultat = executionCrud(stmt)
    print("Data updated succ")
    return resultat

