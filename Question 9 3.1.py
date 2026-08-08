books=[]
while True:
    book=str(input("Enter name of borrowed book (or press Enter to finish):"))
    if book =="":
        break
    books.append(book)

print(f"These are the books you have borrowed: {books}")
