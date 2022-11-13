def delete(list_, index=-1):  # пусть у переменной index аргумент по умолчанию равен -1, вместо None
    if index < 0:
        index += len(list_)
    return list_[:index] + list_[index + 1:]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
