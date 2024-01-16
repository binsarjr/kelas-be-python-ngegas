from db import conn


def get_all_by_product(product_id: int):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id, product_id, image FROM product_images WHERE product_id=%s",
            (product_id,),
        )
        items = []
        for item in cursor.fetchall():
            items.append(
                {
                    "id": item[0],
                    "product_id": item[1],
                    "image": item[2],
                }
            )

        return items


def get_by_id(id: int):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id, product_id, image FROM product_images WHERE id=%s",
            (id,),
        )
        item = cursor.fetchone()
        if item is None:
            return None

        return {
            "id": item[0],
            "product_id": item[1],
            "image": item[2],
        }


def create(product_id: int, image: str):
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO product_images (product_id, image) VALUES (%s, %s)",
            (product_id, image),
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


def delete(id: int):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM product_images WHERE id=%s", (id,))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
