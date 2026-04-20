from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from bson.objectid import ObjectId
from app import mongo
from datetime import datetime

tasks_bp = Blueprint("tasks", __name__)
# Flask, a Blueprint is a way to organize your application into smaller parts (modules).

@tasks_bp.route("/")
def view_tasks():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    # Fetch tasks for the current user
    user_id = session["user_id"]
    tasks_cursor = mongo.db.tasks.find({"user_id": user_id})
    tasks = []
    
    for task in tasks_cursor:
        # Template needs to access task.id and task.name and task.status
        # In dict this is task['id'] but jinja allows task.id for dict keys if accessed as an attribute, wait, Jinja2 allows dict item access via dot notation.
        task["id"] = str(task["_id"])
        tasks.append(task)

    return render_template("task.html", tasks=tasks)


@tasks_bp.route("/add", methods=["POST"])
def add_task():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    title = request.form.get("title")
    if title:
        new_task = {
            "name": title, 
            "status": "Pending", 
            "user_id": session["user_id"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        mongo.db.tasks.insert_one(new_task)
        flash("Task added successfully.", "success")

    return redirect(url_for("tasks.view_tasks"))


@tasks_bp.route("/toggle/<task_id>", methods=["POST"])
def toggle_status(task_id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    try:
        task = mongo.db.tasks.find_one({"_id": ObjectId(task_id), "user_id": session["user_id"]})
        
        if task:
            if task.get("status") == "Pending":
                new_status = "Working"
            elif task.get("status") == "Working":
                new_status = "Done"
            else:
                new_status = "Pending"
                
            mongo.db.tasks.update_one(
                {"_id": ObjectId(task_id)}, 
                {"$set": {"status": new_status}}
            )
    except Exception as e:
        print(f"Error toggling status: {e}")

    return redirect(url_for("tasks.view_tasks"))


@tasks_bp.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    try:
        mongo.db.tasks.delete_one({"_id": ObjectId(task_id), "user_id": session["user_id"]})
    except Exception as e:
        print(f"Error deleting task: {e}")

    return redirect(url_for("tasks.view_tasks"))


@tasks_bp.route("/clear", methods=["POST"])
def clear():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    mongo.db.tasks.delete_many({"user_id": session["user_id"]})
    flash("All your tasks were deleted.", "info")
    return redirect(url_for("tasks.view_tasks"))