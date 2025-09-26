from services import (fetchTodoTasks, fetchInProgressTasks, fetchDoneTasks,Delete,updatepriorite,updatestatus)
import tkinter as tk

todos = fetchTodoTasks()
inprogres = fetchInProgressTasks()
done = fetchDoneTasks()

root = tk.Tk()
root.title("PY-Tasks Kanban")
root.geometry("1000x700")
root.configure(bg="#f0f0f0")

statuses = ["TODO", "PENDING", "DONE"]
properties = ["HIGH", "LOW", "MEDIUM"]
frames = {}
for i, status in enumerate(statuses):
    frame = tk.Frame(root, bg="#e0e0e0", bd=2, relief="groove")
    frame.place(relx=i/3, rely=0, relwidth=1/3, relheight=1)
    label = tk.Label(frame, text=status, bg="#007acc", fg="white", font=("Arial", 14, "bold"), pady=10)
    label.pack(fill="x")
    frames[status] = frame

def AddTask(task, frame):
    frameTask = tk.Frame(frame, bg="white", bd=1, relief="solid", padx=5, pady=5)
    frameTask.pack(pady=5, padx=5, fill="x")
    
    tk.Label(
        frameTask,
        text=f"{task['contenu']}\nPriorité: {task.get('priorite','')}",
        bg="white",
        justify="left",
        wraplength=200
    ).pack(side="left", fill="x", expand=True)
    
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
    
    tk.Button(frameTask, text="Delete", bg="red", fg="white", command=deleteTask).pack(side="right", padx=5)


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
