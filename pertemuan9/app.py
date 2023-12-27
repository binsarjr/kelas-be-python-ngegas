import flask
from flask import request
import todos


app = flask.Flask(__name__)


@app.get("/todos")
def get_all_todos():
    return todos.get_all_todos()


@app.get("/todos/<int:id>")
def get_todo_by_id(id):
    todo = todos.get_todo_by_id(id)
    if todo is None:
        return "", 404
    return todo


@app.post("/todos")
def create_new_todo():
    todo = request.form.get("todo")
    is_done = bool(int(request.form.get("is_done")))
    todos.create_new_todo(
        todo,is_done
    )
    return "", 201


@app.put("/todos/<int:id>")
def update_todo_by_id(id):
    if todos.get_todo_by_id(id) is None:
        return "", 404

    todo = request.form.get("todo")
    is_done = bool(int(request.form.get("is_done")))

    todos.update_todo_by_id(
        id,
        todo,
        is_done
    )
    return "", 200


@app.delete("/todos/<int:id>")
def delete_todo_by_id(id):
    if todos.get_todo_by_id(id) is None:
        return "", 404

    todos.delete_todo_by_id(id)
    return "", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=True)
