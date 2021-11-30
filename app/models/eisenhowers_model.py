from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

@dataclass
class Eisenhowers(db.Model):
    id:int
    type:str
    
    __tablename__ = "eisenhowers"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))