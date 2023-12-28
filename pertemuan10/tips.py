# Convert tuple to dictionary

items = [(5, "todo1", True), (6, "todo2", False), (7, "todo3", False)]

new_items = []

for item in items:
    new_item = {"id": item[0], "todo": item[1], "is_done": item[2]}
    new_items.append(new_item)


# for item in new_items:
#     print("ID", item["id"], "Todo", item["todo"])
print(new_items)

# Convert tuple to object
from collections import namedtuple

Todo = namedtuple("Todo", ["id", "todo", "is_done"])

todo_db = (5, "todo1", True)

todo = Todo(*todo_db)
todo = Todo(todo_db[0], todo_db[1], todo_db[2])


todo = Todo(**{"id": todo_db[0], "todo": todo_db[1], "is_done": todo_db[2]})

# yang digunakan
todo = Todo(
    id=todo_db[0],
    todo=todo_db[1],
    is_done=todo_db[2],
)


new_items = []

for item in items:
    new_item = Todo(
        id=item[0],
        todo=item[1],
        is_done=item[2],
    )
    new_items.append(new_item)

print(new_items)
