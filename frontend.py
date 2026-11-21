#this is frontend is created by mahesh
#this is code written by mahesh 
import tkinter as tk
from tkinter import messagebox


# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()
root.title("Team Task Boards")
root.geometry("1100x650")
root.configure(bg="#f4f6f9")


# -----------------------------
# COLORS
# -----------------------------

SIDEBAR = "#111827"
WHITE = "#ffffff"
BG = "#f4f6f9"
TEXT = "#172033"
GRAY = "#6b7280"
PRIMARY = "#6366f1"
TODO = "#e9edf3"


# -----------------------------
# SIDEBAR
# -----------------------------

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

logo = tk.Label(
    sidebar,
    text="TeamTask",
    bg=SIDEBAR,
    fg=WHITE,
    font=("Arial", 20, "bold")
)

logo.pack(
    pady=30
)


def menu_button(text):
    button = tk.Button(
        sidebar,
        text=text,
        bg=SIDEBAR,
        fg="#cbd5e1",
        activebackground="#252d3d",
        activeforeground=WHITE,
        relief="flat",
        anchor="w",
        padx=25,
        font=("Arial", 11),
        width=20
    )

    button.pack(
        pady=4
    )

    return button


menu_button("▦  Task Board")
menu_button("✓  My Tasks")
menu_button("✓  Completed")
menu_button("♟  Members")
menu_button("⚙  Settings")


# -----------------------------
# MAIN AREA
# -----------------------------

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    side="left",
    fill="both",
    expand=True
)


# -----------------------------
# TOP BAR
# -----------------------------

topbar = tk.Frame(
    main,
    bg=WHITE,
    height=65
)

topbar.pack(
    fill="x"
)

search = tk.Entry(
    topbar,
    width=35,
    font=("Arial", 11),
    relief="solid",
    bd=1
)

search.insert(
    0,
    "Search tasks..."
)

search.pack(
    side="left",
    padx=25,
    pady=18
)

profile = tk.Label(
    topbar,
    text="Alex Morgan   ●",
    bg=WHITE,
    fg=TEXT,
    font=("Arial", 11, "bold")
)

profile.pack(
    side="right",
    padx=25
)


# -----------------------------
# CONTENT
# -----------------------------

content = tk.Frame(
    main,
    bg=BG
)

content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=25
)


# -----------------------------
# HEADER
# -----------------------------

header = tk.Frame(
    content,
    bg=BG
)

header.pack(
    fill="x"
)

title = tk.Label(
    header,
    text="Team Task Board",
    bg=BG,
    fg=TEXT,
    font=("Arial", 25, "bold")
)

title.pack(
    side="left"
)


def add_task():
    messagebox.showinfo(
        "Add Task",
        "Task creation form can be added here."
    )


add_button = tk.Button(
    header,
    text="+ Add Task",
    command=add_task,
    bg=PRIMARY,
    fg=WHITE,
    activebackground="#4f46e5",
    relief="flat",
    padx=18,
    pady=8,
    font=("Arial", 10, "bold")
)

add_button.pack(
    side="right"
)


subtitle = tk.Label(
    content,
    text="Manage your team's work and track project progress.",
    bg=BG,
    fg=GRAY,
    font=("Arial", 10)
)

subtitle.pack(
    anchor="w",
    pady=(5, 20)
)


# -----------------------------
# STATS
# -----------------------------

stats = tk.Frame(
    content,
    bg=BG
)

stats.pack(
    fill="x",
    pady=(0, 20)
)


def create_stat(parent, title, value):
    frame = tk.Frame(
        parent,
        bg=WHITE,
        width=180,
        height=80
    )

    frame.pack(
        side="left",
        padx=(0, 15)
    )

    frame.pack_propagate(False)

    tk.Label(
        frame,
        text=title,
        bg=WHITE,
        fg=GRAY,
        font=("Arial", 9)
    ).pack(
        anchor="w",
        padx=15,
        pady=(12, 2)
    )

    tk.Label(
        frame,
        text=value,
        bg=WHITE,
        fg=TEXT,
        font=("Arial", 20, "bold")
    ).pack(
        anchor="w",
        padx=15
    )


create_stat(stats, "Total Tasks", "12")
create_stat(stats, "In Progress", "4")
create_stat(stats, "Completed", "5")
create_stat(stats, "Team Members", "6")


# -----------------------------
# TASK BOARD
# -----------------------------

board = tk.Frame(
    content,
    bg=BG
)

board.pack(
    fill="both",
    expand=True
)


def create_column(parent, title, tasks):

    column = tk.Frame(
        parent,
        bg=TODO,
        width=220
    )

    column.pack(
        side="left",
        fill="both",
        expand=True,
        padx=5
    )

    column.pack_propagate(False)

    heading = tk.Frame(
        column,
        bg=TODO
    )

    heading.pack(
        fill="x",
        padx=12,
        pady=12
    )

    tk.Label(
        heading,
        text=title,
        bg=TODO,
        fg=TEXT,
        font=("Arial", 12, "bold")
    ).pack(
        side="left"
    )

    tk.Label(
        heading,
        text=str(len(tasks)),
        bg="#d6dbe3",
        fg=GRAY,
        font=("Arial", 9),
        padx=6
    ).pack(
        side="right"
    )

    for task in tasks:

        card = tk.Frame(
            column,
            bg=WHITE,
            height=100
        )

        card.pack(
            fill="x",
            padx=10,
            pady=5
        )

        card.pack_propagate(False)

        priority = task[0]
        name = task[1]
        description = task[2]

        if priority == "HIGH":
            priority_color = "#dc2626"
        elif priority == "MEDIUM":
            priority_color = "#d97706"
        else:
            priority_color = "#16a34a"

        tk.Label(
            card,
            text=priority,
            bg=WHITE,
            fg=priority_color,
            font=("Arial", 8, "bold")
        ).pack(
            anchor="w",
            padx=12,
            pady=(10, 3)
        )

        tk.Label(
            card,
            text=name,
            bg=WHITE,
            fg=TEXT,
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=12
        )

        tk.Label(
            card,
            text=description,
            bg=WHITE,
            fg=GRAY,
            font=("Arial", 8)
        ).pack(
            anchor="w",
            padx=12,
            pady=3
        )


# -----------------------------
# TASK DATA
# -----------------------------

todo_tasks = [
    (
        "HIGH",
        "Design dashboard UI",
        "Create the initial dashboard layout."
    ),
    (
        "MEDIUM",
        "Write documentation",
        "Prepare project documentation."
    ),
    (
        "LOW",
        "Update team profile",
        "Add team member information."
    )
]


progress_tasks = [
    (
        "HIGH",
        "Build authentication",
        "Implement login and registration."
    ),
    (
        "MEDIUM",
        "Create API integration",
        "Connect frontend with API."
    )
]


review_tasks = [
    (
        "HIGH",
        "Review landing page",
        "Check UI before release."
    ),
    (
        "LOW",
        "Check accessibility",
        "Review keyboard navigation."
    )
]


done_tasks = [
    (
        "LOW",
        "Setup repository",
        "Create project repository."
    ),
    (
        "MEDIUM",
        "Setup environment",
        "Configure development tools."
    )
]


# -----------------------------
# CREATE BOARD COLUMNS
# -----------------------------

create_column(
    board,
    "To Do",
    todo_tasks
)

create_column(
    board,
    "In Progress",
    progress_tasks
)

create_column(
    board,
    "Review",
    review_tasks
)

create_column(
    board,
    "Done",
    done_tasks
)


# -----------------------------
# RUN APPLICATION
# -----------------------------

root.mainloop()
