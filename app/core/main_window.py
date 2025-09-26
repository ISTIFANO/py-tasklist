from services import (fetchTodoTasks, fetchInProgressTasks,add_task, fetchDoneTasks,Delete,updatepriorite,updatestatus)
import tkinter as tk
from tkinter import *

todos = fetchTodoTasks()
inprogres = fetchInProgressTasks()
done = fetchDoneTasks()

root = tk.Tk()
root.title("PY-Tasks Kanban")
root.geometry("1200x800")
root.configure(bg="#f0f0f0")

statuses = ["TODO", "PENDING", "DONE"]
properties = ["HIGH", "LOW", "MEDIUM"]
frames = {}

scrol = Scrollbar(root)
scrol.pack(side=RIGHT,fill=Y)

header = tk.Label(
    root,
    text="Py-Task",
    bg="#333",
    fg="white",
    font=("Arial", 20, "bold"),
    pady=15
)
header.pack(fill="x")

def submit_task(): 
    add_task(getContent.get())
    Affichage()
    return 

tk.Label(root, text="Task content:", bg="#f9f9f9", font=("Arial", 12)).pack(pady=5)
getContent = tk.Entry(root, width=30)
getContent.pack(pady=5)

submitBtn = tk.Button(root, text="Submit", command=submit_task, bg="#5B4CAF", fg="white", font=("Arial", 10))
submitBtn.pack(pady=10)


for i, status in enumerate(statuses):
    frame = tk.Frame(root, bg="#e0e0e0", bd=2, relief="groove")
    frame.place(relx=i/3, rely=0.25, relwidth=1/3, relheight=0.75) 
    label = tk.Label(frame, text=status, bg="#007acc", fg="white", font=("Arial", 14, "bold"), pady=10)
    label.pack(fill="x")
    frames[status] = frame

def AddTask(task, frame):
    frameTask = tk.Frame(frame, bg="white", bd=1, relief="solid", padx=13, pady=16)
    frameTask.pack(pady=5, padx=9, fill="x")
    
    tk.Label(
        frameTask,
        text=f"{task['contenu']}\nPriorité: {task.get('priorite','')}",
        bg="white",
        justify="left",
        font="Arial",
        wraplength=400
    ).pack(side="top", fill="x", expand=True)
    
    getStatus = tk.StringVar(value=task.get("status", "TODO"))
    getProritie = tk.StringVar(value=task.get("priorite", "LOW"))

    def statusChanged(new_value):
        updatestatus(task['id'],new_value)
        Affichage()

    def propertyChanged(new_value):
        updatepriorite(task['id'],new_value)
        Affichage()

    def deleteTask():
        Delete(task["id"])
        Affichage()

    tk.OptionMenu(frameTask, getStatus, *statuses, command=statusChanged).pack(side="right", padx=5)
    tk.OptionMenu(frameTask, getProritie, *properties, command=propertyChanged).pack(side="right", padx=5)
    
    tk.Button(frameTask, text="Delete", bg="red", fg="white", command=deleteTask).pack(side="bottom", padx=2,pady=3)


def Affichage():
    global todos,inprogres,done

    todos = fetchTodoTasks()
    inprogres = fetchInProgressTasks()
    done = fetchDoneTasks()

    for status in statuses:
        clearFrame(frames[status])
    
    for task in todos:
        AddTask(task, frames["TODO"])
    for task in inprogres:
     AddTask(task, frames["PENDING"])
    for task in done:
     AddTask(task, frames["DONE"])


def clearFrame(frame):
         for widget in frame.winfo_children():
             if widget != frame.winfo_children()[0]:
              widget.destroy()


Affichage()
root.mainloop()
