# Doc string
# Buatkan sebuah narasi dokumentasi untuk docstring di python
# Docstring adalah cara penulisan dokumentasi di python atau bisa juga untuk menulisakan string yang memiliki banyak baris

bio = '''
Nama: Asep 
Umur: 20
Alamat: Jakarta

'''

# atau bisa juga untuk dokumentasi,misalkan dalam sebuah fungsi

def tambah(angka1, angka2):
  """
  Fungsi ini untuk menambahkan 2 angka
  """
  return angka1 + angka2


#####################
# Penulisan komentar dalam jinja digunakan untuk menghindari data sensitive tampil di source code html yang ditampilkan di browser


# https://media.geeksforgeeks.org/wp-content/uploads/20210625160610/urldiag.PNG

## TIPS: Tambah data item list dari depan

item = [3,4,5]
item = [1,2]+ item