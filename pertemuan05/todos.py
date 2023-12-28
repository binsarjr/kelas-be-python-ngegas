# Initialize the database
todos = [
  {
    "id": 1,
    "todo": "Buy groceries",
  },
]

"""
Digunakan untuk mengetahui id terakhir
Untuk increment id dari data todos
Sehingga untuk data data berikutnya akan di tambah 1 id nya 
"""
last_id = len(todos)
def get_all():
  """
  Digunakan untuk mengambil semua data todos
  """
  return todos


def create(todo):
  """
  Digunakan untuk menambahkan data todos
  """
  global last_id
  last_id += 1

  todos.append({
    "id": last_id,
    "todo": todo
  })


def edit(id, new_todo):
  """
  Digunakan untuk mengedit data todos.
  Id digunakan sebagai penanda untuk mencari nilai yang sama
  didalam list todos.
  Ketika ditemukan kita berhentikan loopingnya dan ubah datanya
  berdasarlkan indexnya
  """
  for index,todo in enumerate(todos):
    if todo['id'] == id:
      todos[index]['todo'] = new_todo
      break


def delete(id):
  """
  Digunakan untuk menghapus data todos.
  Id digunakan sebagai penanda untuk mencari nilai yang sama
  didalam list todos.
  Ketika ditemukan kita berhentikan loopingnya dan hapus datanya
  berdasarlkan indexnya
  """
  for index,todo in enumerate(todos):
    if todo['id'] == id:
      todos.pop(index)
      break