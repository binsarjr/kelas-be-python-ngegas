from flask import Flask, request
import todos


app = Flask(__name__)

# Untuk mengambil semua data todos
@app.get('/todos')
def get_all(): 
  items =  todos.get_all()

  # Jika query string keyword terisi, maka lakukan filter
  if request.args.get('keyword') is not None:
    keyword = request.args.get('keyword')

    _items = []
    for item in items:
      if keyword in item['todo'].lower():
        _items.append(item)
    
    items=_items

  return items


# MMultiple Query String search
@app.get('/todos/searchs')
def get_all_searchs(): 
  items =  todos.get_all()

  # Jika query string keyword terisi, maka lakukan filter
  if len(request.args.getlist('keyword')) > 0:
    keywords = request.args.getlist('keyword')

    _items = []
    for keyword in keywords:
      for item in items:
        if keyword in item['todo'].lower():
          _items.append(item)
    
    items=_items

  return items

# Untuk menambahkan data todos
@app.post('/todos')
def create():
  todo = request.form.get('todo')
  todos.create(todo)
  return "", 201

# Untuk mengambil data todos berdasarkan id
@app.get('/todos/<int:todo_id>')
def get_by_id(todo_id):
  todo = todos.get_by_id(todo_id)
  if todo is None:
    return "", 404
  return todo

# Untuk mengedit data todos berdasarkan id
@app.put('/todos/<int:todo_id>')
def edit(todo_id):
  # Cek apakah data todos dengan id yang diberikan ada
  if todos.get_by_id(todo_id) is None:
    return "", 404
  
  new_todo = request.form.get('todo')
  todos.edit(todo_id, new_todo)
  return "", 202

@app.delete('/todos/<int:todo_id>')
def delete_todo(todo_id):
  # Cek apakah data todos dengan id yang diberikan ada
  if todos.get_by_id(todo_id) is None:
    return "", 404

  todos.delete(todo_id)
  return "", 204


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5001)