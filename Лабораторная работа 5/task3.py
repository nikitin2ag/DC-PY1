from random import randint


def get_unique_list_numbers(start=-10, end=10, size=15) -> list[int]:
    unique_list_numbers = []
    if size > end - start + 1:
        raise ValueError("Размер списка должен быть не больше количества целых чисел в диапазоне!")
    if start > end:
        raise ValueError('Начало диапазона должно быть не больше конца!')
    while len(unique_list_numbers) < size:
        random_number = randint(start, end)
        if random_number not in unique_list_numbers:
            unique_list_numbers.append(random_number)
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers(2, 10, 3)  # в скобках можно указать произвольные значения (start, end, size)
print(list_unique_numbers)  # выводим список из 15 случайных неповторяющихся целых чисел от -10 до 10 включительно
print(len(list_unique_numbers) == len(set(list_unique_numbers)))  # True
