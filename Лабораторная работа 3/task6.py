list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#находим индекс максимального элемента
max_number = list_numbers[0]
for i, number in enumerate(list_numbers):
    if number > max_number:
        max_number = number
        index = i

#меняем местами максимальный и последний элементы
list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]

print(list_numbers)
