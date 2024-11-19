import tkinter as tk
from tkinter import messagebox
import csv

# File for storing tasks
CSV_FILE = "tasks.csv"

# Functionality
task_widgets = []  # List to store task widgets (checkbox, label)


def load_tasks():
    """Load tasks from the CSV file"""
    try:
        with open(CSV_FILE, newline='', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  # Ensure row has two elements
                    add_task_to_frame(row[0], checked=(row[1] == "1"))
    except FileNotFoundError:
        pass  # If no file exists, start with an empty list


def save_tasks():
    """Save tasks to the CSV file"""
    tasks = []
    for task_var, task_label in task_widgets:
        tasks.append([task_label.cget("text"), task_var.get()])
    with open(CSV_FILE, newline='', mode='w') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)


def add_task(event=None):
    """Add a new task to the list"""
    task_text = task_entry.get()
    if task_text:
        add_task_to_frame(task_text)
        task_entry.delete(0, tk.END)
        save_tasks()  # Save after adding
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")


def add_task_to_frame(task_text, checked=False):
    """Helper function to add a task with checkbox"""
    task_var = tk.IntVar(value=1 if checked else 0)  # Checkbox state
    task_frame = tk.Frame(tasks_inner_frame, bg="#e0e0e0", pady=2, padx=5, relief="raised", bd=1)

    task_checkbox = tk.Checkbutton(task_frame, variable=task_var, bg="#e0e0e0", relief="flat")
    task_checkbox.pack(side=tk.LEFT)

    task_label = tk.Label(task_frame, text=task_text, font=("Arial", 12), bg="#e0e0e0")
    task_label.pack(side=tk.LEFT, padx=5)

    task_frame.pack(anchor="w", fill="x", padx=10, pady=2)
    task_widgets.append((task_var, task_label))

    # Add hover effect
    def on_enter(e):
        task_frame['bg'] = '#d0d0d0'
        task_checkbox['bg'] = '#d0d0d0'
        task_label['bg'] = '#d0d0d0'

    def on_leave(e):
        task_frame['bg'] = '#e0e0e0'
        task_checkbox['bg'] = '#e0e0e0'
        task_label['bg'] = '#e0e0e0'

    task_frame.bind("<Enter>", on_enter)
    task_frame.bind("<Leave>", on_leave)
    task_checkbox.bind("<Enter>", on_enter)
    task_checkbox.bind("<Leave>", on_leave)
    task_label.bind("<Enter>", on_enter)
    task_label.bind("<Leave>", on_leave)


def delete_task():
    """Delete the selected tasks"""
    for task_var, task_label in task_widgets[:]:
        if task_var.get() == 1:  # Checked task
            task_label.master.destroy()  # Destroy the frame containing the task
            task_widgets.remove((task_var, task_label))
    save_tasks()  # Save after deleting


def clear_all_tasks():
    """Clear all tasks"""
    for task_var, task_label in task_widgets[:]:
        task_label.master.destroy()  # Destroy the frame containing the task
        task_widgets.remove((task_var, task_label))
    save_tasks()  # Save after clearing all tasks


# GUI Setup
root = tk.Tk()
root.title("To-Do List App")

# Make window resizable
root.geometry("400x500")
root.minsize(300, 400)
root.config(bg="#f0f0f0")

# Task Entry Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(fill="x", pady=5)

label = tk.Label(frame, text="Task:", font=("Arial", 12), bg="#f0f0f0")
label.pack(side=tk.LEFT, padx=5)

task_entry = tk.Entry(frame, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, fill="x", expand=True, padx=5)

# Bind the Enter key to add tasks
task_entry.bind("<Return>", add_task)

button = tk.Button(frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4CAF50", fg="white", relief="flat")
button.pack(side=tk.LEFT, padx=5)

# Tasks Frame
tasks_frame = tk.Frame(root, bg="#f0f0f0")
tasks_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Add a scrollbar for the tasks frame
tasks_scrollbar = tk.Scrollbar(tasks_frame, orient="vertical")
tasks_scrollbar.pack(side=tk.RIGHT, fill="y")

tasks_canvas = tk.Canvas(tasks_frame, bg="#f0f0f0", yscrollcommand=tasks_scrollbar.set)
tasks_canvas.pack(side=tk.LEFT, fill="both", expand=True)
tasks_scrollbar.config(command=tasks_canvas.yview)

tasks_inner_frame = tk.Frame(tasks_canvas, bg="#f0f0f0")
tasks_canvas.create_window((0, 0), window=tasks_inner_frame, anchor="nw")


def on_frame_configure(event):
    tasks_canvas.configure(scrollregion=tasks_canvas.bbox("all"))


tasks_inner_frame.bind("<Configure>", on_frame_configure)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(fill="x", pady=5)

delete_task_button = tk.Button(buttons_frame, text="Delete Selected", command=delete_task, font=("Arial", 12), bg="#FF5733", fg="white", relief="flat")
delete_task_button.pack(side=tk.LEFT, padx=10)

clear_all_tasks_button = tk.Button(buttons_frame, text="Clear All", command=clear_all_tasks, font=("Arial", 12), bg="#f44336", fg="white", relief="flat")
clear_all_tasks_button.pack(side=tk.RIGHT, padx=10)

# Load tasks from CSV after defining the listbox
load_tasks()

# Start the Application
root.mainloop()
