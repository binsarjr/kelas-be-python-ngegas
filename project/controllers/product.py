from models import (
    product as product_model,
    category as category_model,
    product_image as product_image_model,
)
from flask import request


def get_all():
    return product_model.get_all()


def find_by_id(product_id: int):
    product = product_model.find_by_id(product_id)
    if product is None:
        return {"message": "Product not found"}, 404

    return product


def find_product_images_by_product_id(product_id: int):
    product_images = product_image_model.get_all_by_product(product_id)

    return product_images


def create():
    name = request.form.get("name")
    thumbnail = request.files.get("thumbnail")
    stock = request.form.get("stock")
    category_id = request.form.get("category_id")
    description = request.form.get("description")
    price = request.form.get("price")

    if name is None:
        return {"message": "Name is required"}, 400
    if thumbnail is None:
        return {"message": "Thumbnail is required"}, 400
    if stock is None:
        return {"message": "Stock is required"}, 400
    if category_id is None:
        return {"message": "Category is required"}, 400
    # validate category exists in database
    category = category_model.find_by_id(category_id)
    if category is None:
        return {"message": "Category not found"}, 404

    if description is None:
        return {"message": "Description is required"}, 400
    if price is None:
        return {"message": "Price is required"}, 400

    # process thumbnail save to static/uploads
    # validate thumbnail is image only
    if thumbnail.content_type not in ["image/jpeg", "image/png"]:
        return {"message": "Thumbnail must be image only"}, 400

    thumbnail_location = "static/uploads/" + thumbnail.filename
    thumbnail.save(thumbnail_location)

    product_model.create(
        name=name,
        thumbnail=thumbnail_location,
        stock=stock,
        category_id=category_id,
        description=description,
        price=price,
    )

    # create_product_images(product_id=product_id)

    return {"message": "Product created"}, 201


def create_product_images(product_id: int):
    images = request.files.getlist("images")
    if images is None:
        return {"message": "Images is required"}, 400

    # validate product exists in database
    product = product_model.find_by_id(product_id)
    if product is None:
        return {"message": "Product not found"}, 404

    for image in images:
        # validate thumbnail is image only
        if image.content_type not in ["image/jpeg", "image/png"]:
            return {"message": "Images must be image only"}, 400

        image_location = "static/uploads/" + image.filename
        image.save(image_location)

        product_image_model.create(product_id, image_location)

    return {"message": "Product images created"}, 201
