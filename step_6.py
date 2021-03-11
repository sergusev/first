# бесконечный итератор, генерирующий целые числа,  начиная с указанного
from itertools import count
for el in count(int(input('Введите число '))):
    print(el)
# бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее
from itertools import cycle
new_list = ['Hello world', 3.4, 999]
for el in cycle(new_list):
    print(el)