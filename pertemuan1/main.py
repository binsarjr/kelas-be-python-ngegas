

# Apa itu statement?
## Statement adalah sebuah perintah yang akan dieksekusi oleh komputer
## Contoh statement:
### print("Hello World")
### x = 10
### y = 20
### z = x + y

# Apa itu komentar?
## Komentar adalah sebuah penjelasan yang ditulis di dalam kode program
## Komentar tidak akan dieksekusi oleh komputer
## Komentar hanya bisa dibaca oleh programmer
## Komentar digunakan untuk memudahkan programmer dalam memahami kode program
## Komentar tidak akan mempengaruhi kode program
## Komentar hanya bisa ditulis di dalam kode program


# Apa itu assignment
## Assignment adalah sebuah perintah untuk menyimpan data ke dalam sebuah variabel
## Assignment menggunakan tanda sama dengan (=)
## Assignment bisa digunakan untuk menyimpan tipe data primitif
## Assignment bisa digunakan untuk menyimpan tipe data non-primitif


# Apa itu tipe data?
## Tipe data adalah sebuah jenis data yang tersimpan di dalam sebuah variabel
## Tipe data digunakan untuk menentukan jenis data yang akan disimpan di dalam sebuah variabel
## Tipe data digunakan untuk menentukan jenis data yang akan diolah oleh komputer
## Tipe data digunakan untuk menentukan jenis data yang akan ditampilkan ke layar



# TIpe Data Primitif
## String
## Integer
## Float
## Boolean

"Binsar" # String
20 # Integer
20.5 # Float
True # Boolean

# Variabel
## Nama variabel tidak boleh diawali dengan angka
## Nama variabel tidak boleh mengandung spasi
## Nama variabel tidak boleh mengandung simbol, kecuali underscore (_)
## Nama variabel tidak boleh mengandung kata kunci (keyword) dari bahasa pemrograman
nama = "Binsar"
umur = 20
alamat = "Jakarta"
isMarried = False

# print digunakan untuk menampilkan data ke terminal
print(nama, umur, alamat, isMarried)


# Aritmatika
## Penjumlahan (+)
## Pengurangan (-)
## Perkalian (*)
## Pembagian (/)
## Modulus (%)
## Pangkat (**)
## Floor Division (//)

### Contoh Aritmatika
print(10 + 10)
print(10 - 5)
print(10 * 10)
print(10 / 5)
print(10 % 3)
print(10 ** 2)
print(10 // 3)


# Operator Perbandingan
## Sama dengan (==)
## Tidak sama dengan (!=)
## Lebih besar dari (>)
## Lebih kecil dari (<)
## Lebih besar sama dengan (>=)
## Lebih kecil sama dengan (<=)

### Contoh Operator Perbandingan
print(10 == 10)
print(10 != 10)
print(10 > 10)
print(10 < 10)
print(10 >= 10)
print(10 <= 10)

# Operator Logika
## And
## Or
## Not

### Contoh Operator Logika
print(True and True) # True
print(True and False) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or False) # False
print(not True) # False
print(not False) # True

# Operator Assignment
## =
## +=
## -=
## *=
## /=
## %=
## **=
## //=

### Contoh Operator Assignment
x = 10
x += 10 # x = x + 10
print(x)

x -= 10 # x = x - 10
print(x)

x *= 10 # x = x * 10
print(x)

x /= 10 # x = x / 10
print(x)

x %= 10 # x = x % 10
print(x)

x **= 10 # x = x ** 10
print(x)

x //= 10 # x = x // 10
print(x)


# Operator Identitas
## is
## is not

### Contoh Operator Identitas
print(10 is 10) # True
print(10 is not 10) # False
print(10 is 20) # False
print(10 is not 20) # True

# Operator Keanggotaan
## in
## not in

### Contoh Operator Keanggotaan
print("a" in "Binsar") # True
print("a" not in "Binsar") # False
print("b" in "Binsar") # False
print("b" not in "Binsar") # True


# If/Else
## If/Else digunakan untuk mengeksekusi sebuah kode program jika kondisi bernilai True
## If/Else digunakan untuk mengeksekusi sebuah kode program jika kondisi bernilai False
## If/Else digunakan untuk mengeksekusi sebuah kode program jika kondisi bernilai True dan False

### Contoh If/Else
if 10 > 5:
  print("10 lebih besar dari 5")
else:
  print("10 tidak lebih besar dari 5")

# If/Elif/Else
if 10 > 5:
  print("10 lebih besar dari 5")
elif 10 == 5:
  print("10 sama dengan 5")
else:
  print("10 tidak lebih besar dari 5 dan tidak sama dengan 5")


# List
## List adalah sebuah tipe data yang digunakan untuk menyimpan banyak data
## List menggunakan tanda kurung siku ([])
## List bisa menyimpan data dengan tipe data apapun
## List bisa menyimpan data dengan tipe data yang berbeda
## List bisa menyimpan data dengan jumlah yang tidak terbatas
## List bisa menyimpan data dengan indeks yang dimulai dari 0
## List bisa menyimpan data yang sama
## List bersifat mutable, artinya data di dalam list bisa diubah
items = [1, "asep", False, "test4"]
print(items)
print(items[0])
print(items[1])
print(items[2])
print(items[3])

# Tuple
## Tuple adalah sebuah tipe data yang digunakan untuk menyimpan banyak data
## Tuple menggunakan tanda kurung biasa (())
## Tuple bisa menyimpan data dengan tipe data apapun
## Tuple bisa menyimpan data dengan tipe data yang berbeda
## Tuple bisa menyimpan data dengan jumlah yang tidak terbatas
## Tuple bisa menyimpan data dengan indeks yang dimulai dari 0
## Tuple bersifat immutable (tidak bisa diubah)
items = (1, "asep", False, "test4")
print(items)
print(items[0])
print(items[1])
print(items[2])
print(items[3])

# Set
## Set adalah sebuah tipe data yang digunakan untuk menyimpan banyak data
## Set menggunakan tanda kurung kurawal ({})
## Set bisa menyimpan data dengan tipe data apapun
## Set bisa menyimpan data dengan tipe data yang berbeda
## Set bisa menyimpan data dengan jumlah yang tidak terbatas
## Set tidak bisa menyimpan data dengan indeks
## Set tidak bisa menyimpan data yang sama
## Set bersifat mutable, artinya data di dalam set bisa diubah
items = {1, "asep", False, "test4"}
print(items)


# Dictionary
## Dictionary adalah sebuah tipe data yang digunakan untuk menyimpan banyak data
## Dictionary menggunakan tanda kurung kurawal ({})
## Dictionary bisa menyimpan data dengan tipe data apapun
## Dictionary bisa menyimpan data dengan tipe data yang berbeda
## Dictionary bisa menyimpan data dengan jumlah yang tidak terbatas
## Dictionary bersifat mutable, artinya data di dalam dictionary bisa diubah
## Dictionary menggunakan key dan value
## Berbeda dengan Set dan List. Dictionary menggunakan key untuk mengakses data
items = {
  "key1": 1,
  "key2": "asep",
  "key3": False,
  "key4": "test4",
}
print(items)
print(items["key1"])
print(items["key2"])
print(items["key3"])
print(items["key4"])

# Looping
## Looping digunakan untuk mengulang kode program

# For Loop

### Contoh For Loop
# perulangan untuk menampilkan angka 1 sampai 10
for i in range(10):
  print(i)

# perulangan untuk menampilkan angka 10 sampai 20
for i in range(10, 20):
  print(i)

# perulangan untuk menampilkan angka 10 sampai 20 dengan kelipatan 2
for i in range(10, 20, 2):
  print(i)

# perulangan untuk menampilkan angka 20 sampai 10 dengan kelipatan 2
for i in range(20, 10, -2):
  print(i)

## Contoh For Loop dengan List
items = [1, "asep", False, "test4"]
for item in items:
  print(item)

## Contoh For Loop dengan Tuple
items = (1, "asep", False, "test4")
for item in items:
  print(item)

## Contoh For Loop dengan Set
items = {1, "asep", False, "test4"}
for item in items:
  print(item)

## Contoh For Loop dengan Dictionary
items = {
  "key1": 1,
  "key2": "asep",
  "key3": False,
  "key4": "test4",
}
for key in items:
  print(key, items[key])

# While Loop
i = 0
while i < 10:
  print(i)
  i += 1

# Break
## Break digunakan untuk menghentikan perulangan
## Break digunakan untuk menghentikan perulangan jika kondisi bernilai True
## Break digunakan untuk menghentikan perulangan jika kondisi bernilai False
for i in range(10):
  if i == 5:
    break
  print(i)

# Continue
## Continue digunakan untuk melanjutkan perulangan
## Continue digunakan untuk melanjutkan perulangan jika kondisi bernilai True
## Continue digunakan untuk melanjutkan perulangan jika kondisi bernilai False
for i in range(10):
  if i == 5:
    continue
  print(i)


# Case Study program dari semua materi dalam satu program dibawah ini
# Program ini akan menampilkan menu
# Menu:
# 1. Tambah data
# 2. Hapus data
# 3. Tampilkan data
# 4. Keluar
# Pilih menu: 1
# Masukkan nama: Binsar
# Masukkan umur: 20
# Masukkan alamat: Jakarta
# Data berhasil ditambahkan

#  Kode
items = []
while True:
  print("Menu:")
  print("1. Tambah data")
  print("2. Hapus data")
  print("3. Tampilkan data")
  print("4. Keluar")
  menu = int(input("Pilih menu: "))
  if menu == 1:
    nama = input("Masukkan nama: ")
    umur = input("Masukkan umur: ")
    alamat = input("Masukkan alamat: ")
    items.append({
      "nama": nama,
      "umur": umur,
      "alamat": alamat,
    })
    print("Data berhasil ditambahkan")
  elif menu == 2:
    print("Hapus data")
  elif menu == 3:
    print("Tampilkan data")
  elif menu == 4:
    break
  else:
    print("Menu tidak tersedia")
