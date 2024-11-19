# To-Do List Application

This is a simple **To-Do List** application built using Python and Tkinter. The app allows users to add, check off, delete, and clear tasks. Tasks are stored in a CSV file, making them persistent even after the application is closed. The GUI is fully resizable and features a modern, interactive design.

---

## Features

- **Add Tasks**: Enter a task in the input field and press "Add Task" or the Enter key to add it to the list.
- **Check/Uncheck Tasks**: Click the checkbox next to a task to mark it as complete or incomplete.
- **Delete Selected Tasks**: Select tasks using the checkboxes and click "Delete Selected" to remove them.
- **Clear All Tasks**: Remove all tasks from the list with a single button.
- **Persistent Storage**: Tasks are saved in a CSV file (`tasks.csv`) and loaded automatically when the app starts.
- **Responsive GUI**: The interface adjusts dynamically when resized.

---

## How to Run

### Prerequisites

1. Install Python 3.11 or later.
2. Ensure `tkinter` is installed (it comes pre-installed with Python on most systems).

### Steps to Run

1. Download the `app.py` script.
2. Ensure the `tasks.csv` file is in the same directory as the script (or let the app create it automatically).
3. Open a terminal and run:
   ```bash
   python app.py

# File Structure
app.py: The main Python script for the application.
tasks.csv: A CSV file where tasks are stored persistently.
User Guide
Add a Task:

Enter a task in the text field and press Enter or click the "Add Task" button.
Delete Selected Tasks:

Check the tasks you want to delete using the checkboxes, then click "Delete Selected."
Clear All Tasks:

Click "Clear All" to delete all tasks from the list.
Resize the Window:

The app is fully resizable. If tasks are hidden, use the scrollbar to view them.
Design Highlights
Hover Effects: Buttons and task items change color when hovered over for a modern touch.
Scroll Support: Easily manage long lists of tasks with a built-in vertical scrollbar.
Dynamic Layout: The application adjusts its layout based on the window size.


Development
Technologies Used
Python: Core programming language.
Tkinter: For GUI development.
CSV: To store tasks persistently.
Future Improvements
Add due dates and reminders for tasks.
Enhance the design with themes or customizable colors.
Support drag-and-drop for reordering tasks.


# Screenshots
# Main Interface

![](<image2.png>)

![](<image.png>)


"# ToDoList" 
