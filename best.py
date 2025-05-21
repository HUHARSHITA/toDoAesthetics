import tkinter as tk
from tkinter import font
import json
import os
from datetime import datetime

# File to store tasksbest
TASKS_FILE = "tasksFinal.json"

# Load tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add new task
def add_task():
    task_text = task_entry.get()
    if task_text:
        tasks.append({"text": task_text, "done": False})
        task_entry.delete(0, tk.END)
        update_tasks()

# Toggle task (Checkbox)
def toggle_task(event):
    try:
        index = task_list.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        update_tasks()
    except IndexError:
        pass

# Remove selected task
def remove_task():
    try:
        index = task_list.curselection()[0]
        del tasks[index]
        update_tasks()
    except IndexError:
        pass

# Update task list
def update_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "○"
        task_list.insert(tk.END, f"{status} {task['text']}")
    save_tasks()

# Create UI
root = tk.Tk()
root.title("Aesthetic To-Do List")
root.geometry("500x650")
root.configure(bg="#FFF9F3")

tasks = load_tasks()

# Custom Font
title_font = font.Font(family="Comic Sans MS", size=18, weight="bold")
task_font = font.Font(family="Comic Sans MS", size=12)

# 🗓 Display Date
today_date = datetime.today().strftime("%A, %d %B %Y")
tk.Label(root, text=today_date, font=title_font, bg="#FFF9F3", fg="#555").pack(pady=5)

tk.Label(root, text="🌸 To-Do List 🌸", font=title_font, bg="#FFF9F3", fg="#333").pack(pady=5)

# 📌 To-Do List Frame
todo_frame = tk.Frame(root, bg="#FFCBCB", padx=10, pady=10)
todo_frame.pack(pady=10, padx=20, fill="both")

tk.Label(todo_frame, text="Tasks 📝", font=task_font, bg="#FFCBCB", fg="#000").pack(anchor="w")

task_entry = tk.Entry(todo_frame, font=task_font, width=30)
task_entry.pack(pady=5)

btn_frame = tk.Frame(todo_frame, bg="#FFCBCB")
btn_frame.pack()

tk.Button(btn_frame, text="Add ➕", command=add_task, bg="#FF8888", fg="white", font=task_font).pack(side="left", padx=5)
tk.Button(btn_frame, text="Remove ❌", command=remove_task, bg="#D9534F", fg="white", font=task_font).pack(side="left", padx=5)

task_list = tk.Listbox(todo_frame, font=task_font, height=10, width=40, bg="#FFDADA")
task_list.pack()
task_list.bind("<Double-Button-1>", toggle_task)  # Double-click to mark as done

# 📝 Notes Section
notes_frame = tk.Frame(root, bg="#FFA07A", padx=10, pady=10)
notes_frame.pack(pady=10, padx=20, fill="both")

tk.Label(notes_frame, text="Notes 📝", font=task_font, bg="#FFA07A").pack(anchor="w")
notes_text = tk.Text(notes_frame, height=5, width=40, font=task_font, bg="#FFD1B9")
notes_text.pack()

# 🎯 Focus Section
focus_frame = tk.Frame(root, bg="#B0E0E6", padx=10, pady=10)
focus_frame.pack(pady=10, padx=20, fill="both")

tk.Label(focus_frame, text="Focus 🎯", font=task_font, bg="#B0E0E6").pack(anchor="w")
focus_text = tk.Text(focus_frame, height=3, width=40, font=task_font, bg="#D1F1F1")
focus_text.pack()

# 💡 Remember Section (Now Fixed)
remember_frame = tk.Frame(root, bg="#6B8E23", padx=10, pady=10)
remember_frame.pack(pady=10, padx=20, fill="both")

tk.Label(remember_frame, text="Remember 💡", font=task_font, bg="#6B8E23", fg="white").pack(anchor="w")
remember_text = tk.Text(remember_frame, height=2, width=40, font=task_font, bg="#9DC183")
remember_text.pack()

# Load tasks initially
update_tasks()

root.mainloop()
