from flask import Blueprint
from app.controllers.categories_controller import add_category, update_category, delete_category

bp_categories = Blueprint("bp_categories", __name__)

bp_categories.post("/category")(add_category)
bp_categories.patch("/category/<id>")(update_category)
bp_categories.delete("/category/<id>")(delete_category)