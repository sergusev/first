original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(original_list) if original_list[num - 1] < original_list[num]]
print(f'Исходный список {original_list}')
print(f'Новый список {new_list}')