from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.eisenhowers_model import Eisenhowers
    from app.models.tasks_cat_model import TasksCategories
    from app.models.categories_model import Categories
    from app.models.tasks_model import Tasks