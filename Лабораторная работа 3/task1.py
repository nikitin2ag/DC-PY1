src = not False and True or False and not True

# TODO расписать упрощение выражения

# src = True and True or False and False, так как (not False = True) и (not True = False)

# src = True or False, так как (True and True = True) и (False and False = False)

# упрощаем оператор or: src = True

result = True  # TODO подставить результат выражения

print(src == result)
