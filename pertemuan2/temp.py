daging = "kambing" # variabel


def sarapan(lauk):
  def  sayur():
    print("Siapkan sayur")
    print("sayurnya", lauk)
    print("sayurnya", daging)
  print("====ini sayur")
  sayur()
  print("====ini sayur")
  print("Siapkan piring")
  print("Siapkan nasi")
  print("Siapkan lauk")
  print("lauknya", lauk)
  print("daging",daging)

sarapan(daging)
daging = "kuda" # variabel



# # sarapan("ikan")

# # data = {
# #   lauk: "ayam",
# # }

# # sarapan(data["lauk"])







# # print("Siapkan piring")
# # print("Siapkan nasi")
# # print("Siapkan lauk")
# # print("lauknya ayam")


# # print("Siapkan piring")
# # print("Siapkan nasi")
# # print("Siapkan lauk")
# # print("lauknya ikan")


# # print("Siapkan piring")
# # print("Siapkan nasi")
# # print("Siapkan lauk")
# # print("lauknya ayam")
















def luasPersegiPanjang(panjang, lebar):
  print("Menghitung Luas Persegi Panjang")
  luas = panjang * lebar
  print("Panjang: ", panjang) 
  print("Lebar: ", lebar)
  print("Luas: ", luas)

luasPersegiPanjang(20, 10)
luasPersegiPanjang(5, 10)
# luasPersegiPanjang(25, 10)

# def luasPersegi(sisi):
#   return sisi * sisi


# print("===ini luas persgi===")
# print(luasPersegi(10))

# def log(items):
#   for item in items:
#     print("Buah:", item)

# log([
#   "Apel",
#   "Mangga",
#   "Jeruk"
# ])


item  ="binsar"

data = f"asd {item}"



print(data)

bil = 9.2312121

print(f"bilangan {bil:.10f}")
print("bilangan",bil)
