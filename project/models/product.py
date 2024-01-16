from db import conn
import models.category as category_model
import models.product_image as product_image_model


def get_all():
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT produk_id, name, thumbnail, stock, category_id, description, price  FROM products"
        )
        items = []
        for item in cursor.fetchall():
            category = None
            if item[4] is not None:
                category = category_model.find_by_id(item[4])

            items.append(
                {
                    "id": item[0],
                    "name": item[1],
                    "thumbnail": item[2],
                    "stock": item[3],
                    "category_id": item[4],
                    "description": item[5],
                    "price": item[6],
                    "category": category,
                }
            )

        return items


def find_by_id(produk_id: int):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT produk_id, name, thumbnail, stock, category_id, description, price FROM products WHERE produk_id=%s",
            (produk_id,),
        )
        item = cursor.fetchone()
        if item is None:
            return None

        category = None
        if item[4] is not None:
            category = category_model.find_by_id(item[4])

        return {
            "id": item[0],
            "name": item[1],
            "thumbnail": item[2],
            "stock": item[3],
            "category_id": item[4],
            "description": item[5],
            "price": item[6],
            "category": category,
        }


def create(
    name: str,
    thumbnail: str,
    stock: int,
    category_id: int,
    description: str,
    price: int,
):
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO products (name, thumbnail, stock, category_id, description, price) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, thumbnail, stock, category_id, description, price),
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


def update(
    produk_id: int,
    name: str,
    thumbnail: str,
    stock: int,
    category_id: int,
    description: str,
    price: int,
):
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE products SET name=%s, thumbnail=%s, stock=%s, category_id=%s, description=%s, price=%s WHERE produk_id=%s",
            (name, thumbnail, stock, category_id, description, price, produk_id),
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


def delete(produk_id: int):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM products WHERE produk_id=%s", (produk_id,))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
