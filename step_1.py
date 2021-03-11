def sal():
    try:
        a = int(input('Выработка в часах '))
        b = int(input('Ставка в часах '))
        c = int(input('Премия '))
        result = a * b + c
        print(f'Заработная плата сотрудника  {result}')
    except ValueError:
        return print('Введеное значение не число')
sal()