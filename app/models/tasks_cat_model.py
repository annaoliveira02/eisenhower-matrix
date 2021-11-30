from dataclasses import dataclass

from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from app.models.categories_model import Categories
from app.models.tasks_model import Tasks

@dataclass
class TasksCategories(db.Model):
    id:int
    task_id:Tasks
    category_id:Categories
    
    __tablename__ = "tasks_categories"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    task = relationship('Tasks')