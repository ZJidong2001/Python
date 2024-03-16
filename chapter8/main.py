import add
print(add.add(1, 2))


from add import add
print(add(2, 3))


from add import add as a
print(a(3, 4))


import add as a
print(a.add(4, 5))


from add import *
print(add(5, 6))