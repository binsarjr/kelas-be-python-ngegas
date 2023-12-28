from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':

    angka1 = int(request.form.get('angka1'))
    angka2 = int(request.form.get('angka2'))

    return "ini dari post " + str(angka1 + angka2)


  nama = "Binsar Dwi"
  return render_template('index.html', nama=nama)


@app.route('/jinja')
def jinja_view():
  isMarried = True

  secret_key = "aijshndsjakhndkasndjasnkdjn"

  return render_template("jinja.html", isMarried=isMarried,secret_key=secret_key)



# Query Parameter
@app.route("/query")
def belajar_query_parameter():
  # URL: /query?angka1=10&angka2=20
  angka1 = float(request.args.get('angka1'))
  angka2 = float(request.args.get('angka2'))

  aksi = request.args.get('aksi')

  # ?aksi=tambah
  if aksi == "tambah":
    result = angka1 + angka2
  # ?aksi=kurang
  elif aksi == "kurang":
    result = angka1 - angka2
  # ?aksi=kali
  elif aksi == "kali":
    result = angka1 * angka2
  # ?aksi=bagi
  elif aksi == "bagi":
    result = angka1 / angka2
  else:
    result = "Aksi tidak ditemukan"
  
  return "Hasil: "+str(result)


# Flask Route With Variable Rules

# Rule string: Hanya Mengambil string
# Contoh Sukses: /user/binsar
# Contoh Gagal: /user/binsar/1
@app.route('/user/<username>')
def show_user_profile(username):
  return f"User: {username}"

# Rule int: Hanya Mengambil bilangan bulat
# Contoh Sukses: /post/1
# Contoh Gagal: /post/binsar
@app.route('/post/<int:post_id>')
def show_post(post_id):
  return f"Post: {post_id}"

# Rule float: Hanya Mengambil bilangan desimal
# Contoh Sukses: /angka/1.2
# Contoh Gagal: /angka/binsar
@app.route('/angka/<float:angka>')
def show_angka(angka):
  return f"Angka: {angka}"

# Rule path: Mengambil string dengan slash
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
  return f"Subpath: {subpath}"


# Multiple  variable rule
# /blog/20231209/ini-adalah-judul-blog
@app.route('/blog/<int:year>/<judul>')
def blog_detail(judul, year):
  return f"Blog: {year} {judul}"

# Contoh Multiple variable rule dengan kasus tambah angka
@app.route('/aritmatika/<int:angka1>/<int:angka2>/tambah')
def tambah(angka1, angka2):
  return f"Hasil: {angka1 + angka2}"




# python3 -m flask run --reload --debugger
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True,host="0.0.0.0", port=5001)
