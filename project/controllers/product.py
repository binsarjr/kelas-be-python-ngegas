from validators import product as product_validator
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

    validate_errors = product_validator.create_product(
        name=name,
        thumbnail=thumbnail,
        stock=stock,
        category_id=category_id,
        description=description,
        price=price,
    )

    if validate_errors is not None:
        return {"errors": validate_errors}, 422

    thumbnail_location = "static/uploads/" + thumbnail.filename
    thumbnail.save(thumbnail_location)

    last_inserted_product_id = product_model.create(
        name=name,
        thumbnail=thumbnail_location,
        stock=stock,
        category_id=category_id,
        description=description,
        price=price,
    )

    # create_product_images(product_id=product_id)

    return {"message": "Product created", "product_id": last_inserted_product_id}, 201


def update(product_id: int):
    name = request.form.get("name")
    thumbnail = request.files.get("thumbnail")
    stock = request.form.get("stock")
    category_id = request.form.get("category_id")
    description = request.form.get("description")
    price = request.form.get("price")

    validate_errors = product_validator.update_product(
        name=name,
        thumbnail=thumbnail,
        stock=stock,
        category_id=category_id,
        description=description,
        price=price,
    )

    if validate_errors is not None:
        return {"errors": validate_errors}, 422

    product = product_model.find_by_id(product_id)
    if product is None:
        return {"message": "Product not found"}, 404

    thumbnail_location = product["thumbnail"]
    if thumbnail is not None:
        thumbnail_location = "static/uploads/" + thumbnail.filename
        thumbnail.save(thumbnail_location)

    product_model.update(
        product_id=product_id,
        name=name,
        thumbnail=thumbnail_location,
        stock=stock,
        category_id=category_id,
        description=description,
        price=price,
    )

    return {"message": "Product updated"}, 200


def create_product_images(product_id: int):
    images = request.files.getlist("images")

    validate_errors = product_validator.create_product_images(
        images=images, product_id=product_id
    )

    if validate_errors is not None:
        return {"errors": validate_errors}, 422

    for image in images:
        image_location = "static/uploads/" + image.filename
        image.save(image_location)

        product_image_model.create(product_id, image_location)

    return {"message": "Product images created"}, 201
