from flask import Blueprint
from app.controllers.tasks_controller import add_task, update_task, delete_task

bp_tasks = Blueprint("bp_tasks", __name__)

bp_tasks.post("/task")(add_task)
bp_tasks.patch("/task/<id>")(update_task)
bp_tasks.delete("/task/<id>")(delete_task)