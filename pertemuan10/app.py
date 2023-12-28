#!/Users/mymac/miniconda3/bin/python
import flask
from flask import request
import todos
import statuscode
from validator import validate_todo, validate_todo_error, ValidateError


app = flask.Flask(__name__)


@app.get("/todos")
def get_all_todos():
    return todos.get_all_todos()


@app.get("/todos/<int:id>")
def get_todo_by_id(id):
    todo = todos.get_todo_by_id(id)
    if todo is None:
        return "", statuscode.NOT_FOUND
    return todo


@app.post("/todos")
def create_new_todo():
    """
    Contoh validasi menggunakan try except. Yang mana validasinya kita raise lewat fungsi validate_todo_error
    """
    try:
        todo = request.form.get("todo")
        is_done = request.form.get("is_done")
        validate_todo_error(todo, is_done)
        todos.create_new_todo(todo, is_done)
        return "", statuscode.CREATED
    except ValidateError as e:
        return str(e), statuscode.UNPROCESSABLE_ENTITY


@app.put("/todos/<int:id>")
def update_todo_by_id(id):
    """
    Contoh: Validasi menggunakan return. yang mana validasinya kita return lewat fungsi validate_todo jika ada isinya
    """
    if todos.get_todo_by_id(id) is None:
        return "", statuscode.NOT_FOUND

    todo = request.form.get("todo")
    is_done = request.form.get("is_done")

    validate_response = validate_todo(todo, is_done)
    if validate_response is not None:
        return validate_response, statuscode.UNPROCESSABLE_ENTITY

    todos.update_todo_by_id(id, todo, is_done)
    return "", statuscode.OK


@app.delete("/todos/<int:id>")
def delete_todo_by_id(id):
    if todos.get_todo_by_id(id) is None:
        return "", statuscode.NOT_FOUND

    todos.delete_todo_by_id(id)
    return "", statuscode.OK


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=True)
