# Python Dasar

## 1. Tipe Data
Tipe data adalah klasifikasi nilai yang dapat disimpan oleh variabel di dalam suatu program. Python memiliki beberapa tipe data dasar, antara lain:
   - Integer: Bilangan bulat, contohnya 1, 10, -5.
   - Float: Bilangan desimal, contohnya 3.14, 2.5, -0.01.
   - String: Urutan karakter, contohnya "Hello", 'Python'.
   - Boolean: Nilai kebenaran, True atau False.


## 2. Variabel
Variabel digunakan untuk menyimpan nilai. Setiap variabel memiliki tipe data tertentu tergantung pada nilai yang disimpan di dalamnya. Contoh:

```python
nama = "John"
umur = 25
tinggi = 175.5
is_student = True
```

## 3. Operasi Aritmatika
Operasi aritmatika digunakan untuk melakukan operasi matematika pada angka. Beberapa operasi aritmatika dasar meliputi:

- Penjumlahan (+)
- Pengurangan (-)
- Perkalian (*)
- Pembagian (/)
- Modulus (%)
- Pangkat (**)

Contoh:
```python
a = 5
b = 2
hasil = a + b  # 7
```

## 4. Perbandingan

Operasi perbandingan digunakan untuk membandingkan dua nilai dan mengembalikan nilai kebenaran (True atau False). Beberapa operasi perbandingan meliputi:

- Sama dengan (==)
- Tidak sama dengan (!=)
- Lebih besar dari (>)
- Kurang dari (<)
- Lebih besar atau sama dengan (>=)
- Kurang atau sama dengan (<=)

Contoh:
```python
x = 10
y = 5
hasil = x > y  # True
```

```python
nilai = 75
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("Tidak Lulus")
```

## 5. Percabangan

Perabangan digunakan untuk membuat keputusan dalam program berdasarkan kondisi tertentu. Struktur percabangan dalam Python menggunakan kata kunci `if`, `elif`, dan `else`.

```python
nilai = 75
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")
```


## 6. Tipe Data Non-Primitif

Tipe data non-primitif melibatkan struktur data yang lebih kompleks. Beberapa tipe data non-primitif dalam Python meliputi:

- List: Kumpulan elemen yang bisa diubah (mutable).
```python
my_list = [1, 2, 3, "Python", True]

```
- Tuple: Mirip dengan list, tetapi bersifat tidak bisa diubah (immutable).
```python
my_tuple = (1, 2, 3, "Python", True)

```
- Dictionary: Koleksi pasangan kunci-nilai.
```python
my_dict = {"nama": "John", "umur": 25, "tinggi": 175.5}

```
- Set: Kumpulan elemen unik tanpa urutan tertentu.
```python
my_set = {1, 2, 3, 3, 4, 5}
```


## 7. Perulangan

Perulangan memungkinkan eksekusi blok kode tertentu secara berulang. Dalam Python, terdapat dua jenis perulangan utama: `for` dan `while`.

```python
for i in range(5):
    print(i)
```


```python
angka = 0
while angka < 5:
    print(angka)
    angka += 1

```


# Tugas
1. Membuat program untuk menghitung suatu rumus
2. Coba buatkan biodata menggunakan list atau dictionary


Video (harus ada suara, link bisa  di akses)

Poin dalam video:
- Apa itu variabel
- Sebutkan tipe data primitive
- Sebutkan tipe data non primitive
- if else (beserta contoh)
- Loop (beserta contoh)
