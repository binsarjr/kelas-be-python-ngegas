from models import (
    category as category_model,
    product as product_model,
    product_image as product_image_model,
)


def create_product(**kwargs):
    name = kwargs.get("name")
    thumbnail = kwargs.get("thumbnail")
    stock = kwargs.get("stock")
    category_id = kwargs.get("category_id")
    description = kwargs.get("description")
    price = kwargs.get("price")

    errors = []

    if name is None:
        errors.append("Name is required")

    if thumbnail is None:
        errors.append("Thumbnail is required")
    if stock is None:
        errors.append("Stock is required")
    if category_id is None:
        errors.append("Category is required")
    # validate category exists in database
    category = category_model.find_by_id(category_id)
    if category is None:
        errors.append("Category not found")

    if description is None:
        errors.append("Description is required")
    if price is None:
        errors.append("Price is required")

    # process thumbnail save to static/uploads
    # validate thumbnail is image only
    if thumbnail.content_type not in ["image/jpeg", "image/png"]:
        errors.append("Thumbnail must be an image")

    if len(errors) > 0:
        return errors
    return None


def update_product(**kwargs):
    name = kwargs.get("name")
    thumbnail = kwargs.get("thumbnail")
    stock = kwargs.get("stock")
    category_id = kwargs.get("category_id")
    description = kwargs.get("description")
    price = kwargs.get("price")

    errors = []

    if name is None:
        errors.append("Name is required")

    if thumbnail is None:
        errors.append("Thumbnail is required")
    if stock is None:
        errors.append("Stock is required")
    if category_id is None:
        errors.append("Category is required")
    # validate category exists in database
    category = category_model.find_by_id(category_id)
    if category is None:
        errors.append("Category not found")

    if description is None:
        errors.append("Description is required")
    if price is None:
        errors.append("Price is required")

    # process thumbnail save to static/uploads
    # validate thumbnail is image only
    if thumbnail.content_type not in ["image/jpeg", "image/png"]:
        errors.append("Thumbnail must be an image")

    if len(errors) > 0:
        return errors
    return None


def create_product_images(**kwargs):
    images = kwargs.get("images")
    product_id = kwargs.get("product_id")

    errors = []

    if images is None:
        errors.append("Images is required")

    if product_id is None:
        errors.append("Product ID is required")

    # validate images is image only
    for image in images:
        if image.content_type not in ["image/jpeg", "image/png"]:
            errors.append("Images must be image only")

    # validate product exists in database
    product = product_model.find_by_id(product_id)
    if product is None:
        errors.append("Product not found")

    if len(errors) > 0:
        return errors
    return None
