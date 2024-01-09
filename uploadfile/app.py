from flask import Flask, request
import os
import db, time


app = Flask(__name__)


@app.post("/")
def upload():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    if file.content_type not in [
        "image/jpeg",
        "image/jpg",
        "image/webp",
        "image/png",
    ]:
        return "File type not allowed"

    # Save the uploaded file to a specific folder, for example, the 'uploads' folder
    location = "static/uploads/" + str(time.time()) + "_" + file.filename
    file.save(location)

    conn = db.conn.cursor()
    conn.execute("INSERT INTO images (image) VALUES (%s)", (location,))
    db.conn.commit()
    conn.close()

    return "File uploaded successfully"


@app.post("/<int:id>")
def edit_gambar(id):
    # Cek apakah id ada atau tidak
    conn = db.conn.cursor()
    conn.execute("SELECT id, image FROM images WHERE id = %s", (id,))
    item = conn.fetchone()

    db.conn.commit()
    conn.close()

    if item is None:
        return "Image not found"

    data = {"id": item[0], "image": item[1]}

    # Validasi file ada atau tidak
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    location_new = None
    try:
        # Hapus file lama
        if os.path.exists(data["image"]):
            os.remove(data["image"])

        # Simpan file baru
        location_new = "static/uploads/" + str(time.time()) + "_" + file.filename
        file.save(location_new)

        # Update database
        conn = db.conn.cursor()
        conn.execute("UPDATE images SET image = %s WHERE id = %s", (location_new, id))
        db.conn.commit()
        conn.close()
    except Exception as e:
        if location_new is not None:
            os.remove(location_new)
        raise e

    return "File edited successfully"


@app.delete("/<int:id>")
def hapus_gambar(id):
    conn = db.conn.cursor()
    conn.execute("SELECT id, image FROM images WHERE id = %s", (id,))
    item = conn.fetchone()

    db.conn.commit()
    conn.close()

    if item is None:
        return "Image not found"

    data = {"id": item[0], "image": item[1]}

    os.remove(data["image"])

    conn = db.conn.cursor()
    conn.execute("DELETE FROM images WHERE id = %s", (id,))
    db.conn.commit()
    conn.close()

    return "File deleted successfully"


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5001)
