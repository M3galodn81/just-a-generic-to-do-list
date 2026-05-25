import sqlite3 , user_task
from pathlib import Path
from flask import jsonify

DB_NAME = "tasks.db"

def add_task(task: user_task.UserTask):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO tasks (
        title,
        description,
        priority,
        is_done
    )
    VALUES (?, ?, ?, ?)
    """, (
        task.title,
        task.description,
        task.priority.value,
        int(task.is_done)
    ))

    connection.commit()
    connection.close()

    print(f"{task} was added successfully")

def get_tasks():

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    connection.close()

    task_list = []
    for task in tasks:
        task_list.append({
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "priority": task[3],
            "is_done": task[4]
        })

    print(f"Tasks was retrived successfully")
    return jsonify(task_list)

def get_task(task_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchonce()

    connection.close()

    task = {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "priority": task[3],
        "is_done": task[4]
    }

    print(f"Task {task_id} was retrived successfully")
    return jsonify(task)

def mark_task(task_id, is_done):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Yes, I'm leaving this vulnerable so I can practice curl or something like that 
    cursor.execute(f"""
    UPDATE tasks
    SET is_done = {int(is_done)}
    WHERE id = {task_id}
    """)

    # Sanitized version
    # cursor.execute(
    #     "UPDATE tasks SET is_done = ? WHERE id = ?",
    #     (int(is_done), task_id)
    # )

    connection.commit()
    connection.close()

    print(f"Task ID {task_id} was marked successfully")

def update_task(task_id, title, description, priority):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, priority = ? WHERE id = ?",
        (title, description, priority, task_id)
    )
    connection.commit()
    connection.close()

def delete_task(task_id):

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    print(f"Task {task_id} was delete successfully")

