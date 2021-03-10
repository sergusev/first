def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return 'Ошибка! Делить на 0 нельзя'

print(my_func(int(input("Ввести x = ")), int(input("Ввести y = "))))