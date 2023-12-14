# Apa itu fungsi
# Fungsi adalah sebuah blok kode yang dapat digunakan kembali
# Fungsi dapat menerima input dan mengembalikan output
# Fungsi dapat digunakan berulang kali

# Aturan Penulisan Nama Fungsi
# ## Nama fungsi tidak boleh mengandung spasi
# ## Nama fungsi tidak boleh diawali dengan angka
# ## Nama fungsi tidak boleh mengandung simbol, kecuali underscore (_)
# ## Nama fungsi tidak boleh mengandung kata kunci (keyword) dari bahasa pemrograman

# Format penulisan fungsi
# def namaFungsi():
#   print("Hello World")

# Apa itu fungsi void dan non-void
# Fungsi void adalah fungsi yang tidak mengembalikan nilai apapun
# Fungsi non-void adalah fungsi yang mengembalikan nilai apapun

# Membuat Fungsi
# ## Cara 1: void
def myFunction():
  print("Hello World")

myFunction()

# ## Cara 2: non-void
def myFunction():
  return "Hello World"

print(myFunction())

# Parameter
# ## Parameter adalah sebuah nilai yang dilewatkan ke dalam fungsi
# ## Parameter bisa lebih dari satu
# ## Parameter bisa berupa tipe data apapun
# ## Parameter bisa berupa tipe data yang berbeda
# ## Parameter bersifat opsional, artinya fungsi bisa berjalan tanpa parameter

# Contoh 1: Required Parameter
def myFunction(name):
  print("Hello " + name)

myFunction("asep")

# Contoh 2: Required Parameter
def myFunction(name, age):
  print("Hello " + name + ", your age is " + str(age))

myFunction("asep", 20)

# Contoh 3: Keyword Argument
def myFunction(name, age):
  print("Hello " + name + ", your age is " + str(age))

myFunction(age=20, name="asep")

# Contoh 4: Default Parameter
def myFunction(name, age=20):
  print("Hello " + name + ", your age is " + str(age))

myFunction("asep")

# Contoh 5: Default Parameter
def myFunction(name="asep", age=20):
  print("Hello " + name + ", your age is " + str(age))

myFunction()

# Return
# ## Return adalah sebuah nilai yang dikembalikan oleh fungsi
# ## Return bisa berupa tipe data apapun
# ## Return bisa berupa tipe data yang berbeda
# ## Return bersifat opsional, artinya fungsi bisa berjalan tanpa return

# Contoh 1: void
def myFunction():
  print("Hello World")

myFunction()

# Contoh 2: non-void
def myFunction():
  return "Hello World"

print(myFunction())

# Contoh 3: non-void
def myFunction(name):
  return "Hello " + name

print(myFunction("asep"))

# Contoh 4: non-void
def myFunction(name, age):
  return "Hello " + name + ", your age is " + str(age)

print(myFunction("asep", 20))

# Contoh 5: non-void
def myFunction(name, age):
  return "Hello " + name + ", your age is " + str(age)

print(myFunction(age=20, name="asep"))

# Contoh 6: non-void
def myFunction(name, age=20):
  return "Hello " + name + ", your age is " + str(age)

print(myFunction("asep"))

