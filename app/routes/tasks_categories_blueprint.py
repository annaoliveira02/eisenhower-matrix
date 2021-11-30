from flask import Blueprint
from app.controllers.tasks_categories_controller import get_all

bp_all = Blueprint("bp_all", __name__)

bp_all.get("/")(get_all)