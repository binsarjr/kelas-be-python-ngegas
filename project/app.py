from flask import Flask

app = Flask(__name__)


import controllers.category as category_controller


@app.get("/categories")
def categories_all():
    return category_controller.get_all()


@app.get("/categories/<int:category_id>")
def categories_find_by_id(category_id: int):
    return category_controller.find_by_id(category_id)


@app.post("/categories")
def categories_create():
    return category_controller.create()


@app.put("/categories/<int:category_id>")
def categories_update(category_id: int):
    return category_controller.update(category_id)


@app.delete("/categories/<int:category_id>")
def categories_delete(category_id: int):
    return category_controller.delete(category_id)


import controllers.product as product_controller


@app.get("/products")
def products_all():
    return product_controller.get_all()


@app.get("/products/<int:product_id>")
def products_find_by_id(product_id: int):
    return product_controller.find_by_id(product_id)


@app.post("/products")
def products_create():
    return product_controller.create()


@app.post("/products/<int:product_id>/images")
def products_images_create(product_id: int):
    return product_controller.create_product_images(product_id)


@app.get("/products/<int:product_id>/images")
def products_images_find_by_product_id(product_id: int):
    return product_controller.find_product_images_by_product_id(product_id)


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0", use_reloader=True)
