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



if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)