from models import category as category_model
from flask import request


def get_all():
    return category_model.get_all()


def find_by_id(category_id: int):
    category = category_model.find_by_id(category_id)
    if category is None:
        return {"message": "Category not found"}, 404

    return category


def create():
    category = request.form.get("category")
    if category is None:
        return {"message": "Category is required"}, 400
    return category_model.create(category)


def update(category_id: int):
    category = request.form.get("category")
    if category is None:
        return {"message": "Category is required"}, 400

    # check category is exist
    category = category_model.find_by_id(category_id)
    if category is None:
        return {"message": "Category not found"}, 404

    return category_model.update(category_id, category)


def delete(id: int):
    # check category is exist
    category = category_model.find_by_id(id)
    if category is None:
        return {"message": "Category not found"}, 404
    return category_model.delete(id)
