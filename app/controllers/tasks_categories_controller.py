from flask.json import jsonify
from app.models.categories_model import Categories

def get_all():
    categories = Categories.query.all()

    return jsonify([{
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "tasks": [{
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "priority": task.eisenhower_classification.type
            } for task in category.result]
        } for category in categories]), 200