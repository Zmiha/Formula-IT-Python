# TODO Найдите количество книг, которое можно разместить на дискете

discrete = 1.44
page = 100
str_ = 50
symbol = 25
wt = 4

discrete *= 1024 * 1024
wtBook = wt * symbol * str_ * page

maxBook = discrete // wtBook

print("Количество книг, помещающихся на дискету:", int(maxBook))
