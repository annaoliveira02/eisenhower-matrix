from flask import request, current_app
from flask.json import jsonify
from app.exceptions.exceptions import UniqueCategoryError
from app.models.categories_model import Categories

def add_category():
    try:
        data = request.json
        category = Categories(**data)

        current_app.db.session.add(category)
        current_app.db.session.commit()

        return jsonify(category), 201
    
    except UniqueCategoryError:
        return {'msg': 'Category already exists!'}, 409

def update_category(id):
    category = Categories.query.filter(Categories.id==id).one_or_none()

    try:
        current= Categories.query.get(id)
        data = request.get_json()

        if current == None: 
            return{"msg": "Category not found"},404
        for key, value in data.items():
            setattr(current, key, value)
            
        current_app.db.session.add(current)
        current_app.db.session.commit()
        return {
        "id": category.id,
        "name": category.name,
        "description": category.description
        }, 200
    
    except UniqueCategoryError:
        return {'msg': 'Category already exists!'}, 409

def delete_category(id):
    current_category = Categories.query.get(id)

    if current_category == None:
        return {"msg": "Category not found"}, 404

    current_app.db.session.delete(current_category)
    current_app.db.session.commit()

    return "", 204

