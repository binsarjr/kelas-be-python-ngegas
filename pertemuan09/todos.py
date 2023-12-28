# shcmea todos kolom id, todo, is_done
# Buat fungsi CRUD untuk tabel todos dengan return dictionary
from db import conn
from psycopg2.errors import DatabaseError


def get_all_todos():
    cur = conn.cursor()
    try:
        cur.execute("SELECT id,todo,is_done FROM todos")
        todos = cur.fetchall()

        # Convert tuple to dictionary
        new_todos = []
        for todo in todos:
            new_todo = {
                "id": todo[0],
                "todo": todo[1],
                "is_done": todo[2],
            }
            new_todos.append(new_todo)

        conn.commit()
    except DatabaseError:
        conn.rollback()
    finally:
        cur.close()

    return new_todos


def get_todo_by_id(id):
    cur = conn.cursor()

    todo = None
    try:
        cur.execute("SELECT id,todo,is_done FROM todos WHERE id = %s", (id,))
        todo = cur.fetchone()

        conn.commit()
    except DatabaseError:
        conn.rollback()
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


def create_new_todo(new_todo: str, is_done: bool = False) :
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO todos (todo, is_done) VALUES (%s, %s)", (new_todo, is_done)
        )

        conn.commit()
    except DatabaseError:
        conn.rollback()
    finally:
        cur.close()


def update_todo_by_id(id, new_todo: str, is_done: bool = False):
    cur = conn.cursor()
    try:
        cur.execute("UPDATE todos SET todo = %s, is_done = %s WHERE id = %s", (new_todo,is_done, id))
        conn.commit()
    except DatabaseError:
        conn.rollback()
    finally:
        cur.close()


def delete_todo_by_id(id):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM todos WHERE id = %s", (id,))
        conn.commit()
    except DatabaseError:
        conn.rollback()
    finally:
        cur.close()


# print(get_all_todos())
# print(get_todo_by_id(5))


# for todo in get_all_todos():
#     print("id:", todo[0], "todo:", todo[1], "is_done:", todo[2])
