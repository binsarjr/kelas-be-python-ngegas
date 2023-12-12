
while True:
  angka=''
  try:

    inputan = input("Masukkan angka: ")

    angka = int(inputan)
  except ValueError:
    print("Maaf, input harus berupa angka")
  print("Angka",angka)