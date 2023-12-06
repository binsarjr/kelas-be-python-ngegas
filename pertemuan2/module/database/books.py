books = [
  {
    "title": "Buku 1",
    "author": "Author 1"
  }
]

def insertBook(title, author):
  book = {
    "title": title,
    "author": author
  }
  books.append(book)

def showBooks():
  for book in books:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print("")

def deleteBook(title):
  for book in books:
    if book["title"] == title:
      books.remove(book)
      print("Buku", title, "berhasil dihapus")
      return
  print("Buku", title, "tidak ditemukan")
