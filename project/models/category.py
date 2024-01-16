from db import conn


def get_all():
    with conn.cursor() as cursor:
        cursor.execute("SELECT category_id, category FROM categories")
        items = []
        for item in cursor.fetchall():
            items.append({"id": item[0], "category": item[1]})

        return items


def find_by_id(category_id: int):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT category_id, category FROM categories WHERE category_id=%s",
            (category_id,),
        )
        item = cursor.fetchone()
        if item is None:
            return None

        return {"id": item[0], "category": item[1]}


def create(category: str):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO categories (category) VALUES (%s)", (category,))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


def update(category_id: int, category: str):
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE categories SET category=%s WHERE category_id=%s",
            (category, category_id),
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
        cur.execute("DELETE FROM categories WHERE id=%s", (id,))
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
