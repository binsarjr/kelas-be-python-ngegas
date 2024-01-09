from flask import Flask, request, render_template
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)
import todos, statuscode
from validator import *
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import base64

app = Flask(__name__)


@app.get("/todos")
def get_all_todos():
    limit = int(request.args.get("limit", 3))
    page = int(request.args.get("page", 1))

    return todos.get_all_todos(
        limit=limit,
        page=page,
    )


@app.get("/todos/lazy")
def get_all_todos_lazy():
    limit = int(request.args.get("limit", 3))
    cursor = request.args.get("cursor", None)

    last_id = 0

    if cursor is not None:
        last_id = int(base64.b64decode(cursor.encode("utf-8")).decode("utf-8"))

    _todos = todos.get_all_todos_lazy(
        limit=limit,
        last_id=last_id,
    )

    id_terbesar = 0

    for todo in _todos:
        if todo["id"] > id_terbesar:
            id_terbesar = todo["id"]

    print(id_terbesar)

    return {
        "data": _todos,
        "next_id": base64.b64encode(str(id_terbesar).encode("utf-8")).decode("utf-8"),
    }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=True)
