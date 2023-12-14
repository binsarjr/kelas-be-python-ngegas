# Python Lanjutan
## 1. Fungsi (Function) dalam Python
### 1.1 Pengenalan Fungsi
Fungsi adalah blok kode yang dapat dijalankan berulang kali untuk menyelesaikan tugas tertentu. Fungsi membantu mengorganisir dan memecah kode menjadi bagian-bagian yang lebih kecil dan dapat digunakan kembali.

### 1.2 Mendefinisikan Fungsi
Dalam Python, fungsi didefinisikan menggunakan kata kunci def. Contoh:
```python
def sapa():
    print("Halo, selamat datang!")

```

### 1.3 Parameter dan Argumen
Fungsi dapat menerima nilai (parameter) yang diteruskan saat fungsi dipanggil. Contoh:
```python
def sapa(nama):
    print("Halo, " + nama + "!")
sapa("John")

```

### 1.4 Nilai Kembalian
Fungsi dapat mengembalikan nilai dengan menggunakan kata kunci `return`. Contoh:
```python
def tambah(a, b):
    hasil = a + b
    return hasil
total = tambah(3, 5)
print("Hasil penjumlahan:", total)

```

## 2. Modul (Module) dalam Python
### 2.1 Apa itu Modul?
Modul adalah file Python yang berisi definisi dan pernyataan Python. Modul memungkinkan kita untuk mengorganisir kode ke dalam file terpisah untuk memudahkan pemeliharaan dan pengelolaan.

### 2.2 Membuat Modul
Membuat modul sangat sederhana. Buat file baru dengan ekstensi .py, dan masukkan kode Python di dalamnya. Contoh:
```python
# modul_sapa.py
def sapa(nama):
    print("Halo, " + nama + "!")

```

### 2.3 Mengimpor Modul
Gunakan pernyataan import untuk mengimpor modul ke dalam skrip Python Anda. Contoh:
```python
# skrip.py
import modul_sapa
modul_sapa.sapa("John")

```

### 2.4 Menggunakan Alias
Anda dapat memberikan alias saat mengimpor modul untuk mempersingkat penulisan. Contoh:
```python
# skrip.py
import modul_sapa as ms
ms.sapa("John")

```

### 2.5 Mengimpor Fungsi atau Variabel Tertentu
Jika Anda hanya membutuhkan sebagian kecil dari modul, Anda dapat mengimpor fungsi atau variabel tertentu. Contoh:
```python
# skrip.py
from modul_sapa import sapa
sapa("John")

```