from services import (fetchTodoTasks,fetchInProgressTasks,fetchDoneTasks)
import tkinter as tk
from tkinter import ttk

todos = fetchTodoTasks()
inprogres = fetchInProgressTasks()
done = fetchDoneTasks()

print(todos)

root = tk.Tk()
root.title("PY-Tasks Kanban")
root.geometry("800x400")
root.configure(bg="#f0f0f0")

statuses = ["TODO", "In Progress", "Done"]
frames = {}

for i, status in enumerate(statuses):
    frame = tk.Frame(root, bg="#e0e0e0", bd=2, relief="groove")
    frame.place(relx=i/3, rely=0, relwidth=1/3, relheight=1)  
    label = tk.Label(frame, text=status, bg="#007acc", fg="white", font=("Arial", 14, "bold"), pady=10)
    label.pack(fill="x")
    frames[status] = frame

for task in todos:
    tk.Label(
        frames["TODO"],
        text=f"{task['contenu']}\nPriorité: {task.get('priorite','')}",
        bg="white",
        bd=1,
        relief="solid",
        padx=5,
        pady=5,
        wraplength=200,
        justify="left"
    ).pack(pady=5, padx=5, fill="x")
for task in inprogres:
    tk.Label(
        frames["In Progress"],
        text=f"{task['contenu']}\nPriorité: {task.get('priorite','')}",
        bg="white",
        bd=1,
        relief="solid",
        padx=5,
        pady=5,
        wraplength=200,
        justify="left"
    ).pack(pady=5, padx=5, fill="x")

    for task in done:
     tk.Label(
        frames["Done"],
        text=f"{task['contenu']}\nPriorité: {task.get('priorite','')}",
        bg="white",
        bd=1,
        relief="solid",
        padx=5,
        pady=5,
        wraplength=200,
        justify="left"
    ).pack(pady=5, padx=5, fill="x")
root.mainloop()
