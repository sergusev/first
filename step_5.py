import sys

result = 0
while True:
    line = input('Ввести число или ввести q для завершения: ')
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f'Сумма чисел {result}')
                exit(0)
            else:
                print(f'Сумма чисел {result}. Произошла ошибка ввода', file=sys.stderr)
                exit(1)