#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
from flask import Flask
import todos

app = Flask(__name__)


@app.route("/")
def all_todos():
  """
  Routing untuk mengambil semua data todos
  """
  return todos.get_all()

@app.route("/create/<path:todo>")
def create_todo(todo):
  """
  Routing untuk menambahkan data todos
  """
  todos.create(todo)

  return {
    "status": "success",
  }


@app.route("/edit/<int:id>/<path:new_todo>")
def edit(id, new_todo):
  """
  Routing untuk mengedit data todos
  """
  todos.edit(id, new_todo)

  return {
    "status": "success",
  }

@app.route("/delete/<int:id>")
def delete(id):
  """
  Routing untuk menghapus data todos
  """
  todos.delete(id)

  return {
    "status": "success",
  }









if(__name__ == "__main__"):
  app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5001)

