list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

#находим максимальный элемент
max_number = list_numbers[0]
for number in list_numbers:
    if number > max_number:
        max_number = number

#получаем индекс максимального элемента
index = list_numbers.index(max_number)

#меняем местами максимальный и последний элементы
list_numbers[index], list_numbers[-1] = list_numbers[-1], list_numbers[index]

print(list_numbers)
