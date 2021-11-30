from dataclasses import dataclass
from sqlalchemy.orm import relationship, validates
from app.configs.database import db
from app.exceptions.exceptions import UniqueCategoryError

@dataclass
class Categories(db.Model):
    id:int
    name:str
    description:str
    
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, default="")
    result = relationship('Tasks', secondary='tasks_categories', backref='categories')

    @validates('name')
    def validate(self, key, name):
      unique_key = (
              Categories
              .query
              .filter(Categories.name==name)
              .one_or_none()
          )
      if unique_key is not None:
        raise UniqueCategoryError
      return name