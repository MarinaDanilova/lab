# TODO Найдите количество книг, которое можно разместить на дискете
page = 100
line = 50
symbol = 25
code = 4
size_one_book_bite = page * line * symbol * code
size_one_book_mb = round(size_one_book_bite/1048576, 2)
disket = 1.44
books_in_disket = int(round(disket / size_one_book_mb, 0))
print("Количество книг, помещающихся на дискету:", books_in_disket)
