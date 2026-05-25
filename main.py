from flask import Flask, jsonify,request,render_template
import user_task
import db_init, db_methods

# from markupsafe import escape

app = Flask(__name__)

db_init.initialize_database()

# home page
@app.route("/")
def index():
    return render_template("index.html")

# about page
@app.route('/about')
def about():
    return render_template("about.html")

# API ROUTES
# Create a Task
@app.route("/api/tasks", methods=["POST"])
def create_task():

    data = request.json

    task = user_task.UserTask(
        title=data["title"],
        description=data["description"],
        priority=user_task.Priority[data["priority"]]
    )

    db_methods.add_task(task)

    return jsonify({
        "message": "Task added successfully"
    }), 201

# Retrive task
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return db_methods.get_tasks()

@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    return db_methods.get_task(task_id)

@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def mark_task(task_id):
    data = request.get_json()
    is_done = data.get("is_done")
    db_methods.mark_task(task_id, is_done)
    return jsonify({"message": "Task updated successfully"})

# Delete
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    db_methods.delete_task(task_id)
    return jsonify({"message": "Task updated successfully"})



