from app.routes.categories_blueprint import bp_categories
from app.routes.tasks_blueprint import bp_tasks
from app.routes.tasks_categories_blueprint import bp_all
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_tasks)
    app.register_blueprint(bp_all)
