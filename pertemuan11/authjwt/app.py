from flask import Flask, request
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret key boleh random"
jwt = JWTManager(app)


# Contoh endpoint untuk login
@app.route("/login", methods=["POST"])
def login():
    # Lakukan validasi username dan password
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    if username not in "admin" or password != "admin":
        return {"msg": "Username atau password salah"}, 401

    # Jika validasi berhasil, buat access token
    access_token = create_access_token(identity=username)
    return {"access_token": access_token}, 200


# Contoh endpoint yang memerlukan otentikasi
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Mendapatkan identitas user dari token
    current_user = get_jwt_identity()
    return {"logged_in_as": current_user}, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=True)
