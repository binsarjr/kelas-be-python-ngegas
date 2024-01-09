# shcmea todos kolom id, todo, is_done
# Buat fungsi CRUD untuk tabel todos dengan return dictionary
from db import conn
from psycopg2.errors import DatabaseError


def get_all_todos(page: int, limit: int):
    """
    Fungsi untuk menampilkan semua todos
    """
    cur = conn.cursor()
    try:
        page = (page - 1) * limit
        cur.execute(
            f"SELECT id,todo,is_done FROM todos limit %(limit)s offset %(offset)s",
            {"limit": limit, "offset": page},
        )
        todos = cur.fetchall()

        # Convert tuple to dictionary
        # Karena python mereturn tipe data tuple. Maka kita harus mengubahnya menjadi dictionary
        new_todos = []
        for todo in todos:
            new_todo = {
                "id": todo[0],
                "todo": todo[1],
                "is_done": todo[2],
            }
            new_todos.append(new_todo)

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()

    return new_todos


def get_all_todos_lazy(last_id: int, limit: int):
    """
    Fungsi untuk menampilkan semua todos
    """
    cur = conn.cursor()
    try:
        cur.execute(
            f"SELECT id,todo,is_done FROM todos where id > %(last_id)s limit %(limit)s",
            {"limit": limit, "last_id": last_id},
        )
        todos = cur.fetchall()

        # Convert tuple to dictionary
        # Karena python mereturn tipe data tuple. Maka kita harus mengubahnya menjadi dictionary
        new_todos = []
        for todo in todos:
            new_todo = {
                "id": todo[0],
                "todo": todo[1],
                "is_done": todo[2],
            }
            new_todos.append(new_todo)

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()

    return new_todos


def get_todo_by_id(id):
    """
    Fungsi untuk menampilkan todo berdasarkan id
    """
    cur = conn.cursor()

    todo = None
    try:
        # %s adalah placeholder. Jika ada 2 placeholder maka harus ada 2 parameter, harus urut dan harus tuple
        cur.execute("SELECT id,todo,is_done FROM todos WHERE id = %s", (id,))
        todo = cur.fetchone()

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()

    if todo is None:
        return None

    # Convert tuple to dictionary
    return {
        "id": todo[0],
        "todo": todo[1],
        "is_done": todo[2],
    }


def create_new_todo(new_todo: str, is_done: bool = False):
    cur = conn.cursor()
    try:
        cur.execute(
            # %(new_todo)s adalah placeholder. Jika ada 2 placeholder maka harus ada 2 parameter, tidak harus urut dan harus dictionary
            "INSERT INTO todos (todo, is_done) VALUES (%(new_todo)s, %(is_done)s)",
            {
                "new_todo": new_todo,
                "is_done": is_done,
            },
        )

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


def update_todo_by_id(id, new_todo: str, is_done: bool = False):
    cur = conn.cursor()
    try:
        cur.execute(
            # %(new_todo)s adalah placeholder. Jika ada 2 placeholder maka harus ada 2 parameter, tidak harus urut dan harus dictionary
            "UPDATE todos SET todo = %(new_todo)s, is_done = %(is_done)s WHERE id = %(id)s",
            {
                "id": id,
                "is_done": is_done,
                "new_todo": new_todo,
            },
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


def delete_todo_by_id(id):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM todos WHERE id = %s", (id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()


# print(get_all_todos())
# print(get_todo_by_id(5))


# for todo in get_all_todos():
#     print("id:", todo[0], "todo:", todo[1], "is_done:", todo[2])
