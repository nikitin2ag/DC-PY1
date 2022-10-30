def get_count_char(str_):  # функция, возвращающая словарь c количеством каждой буквы в строке
    chars = {}
    for char in str_.lower():
        if char.isalpha():
            chars[char] = chars.get(char, 0) + 1
    return chars


def reformat_in_percent(dict_chars):  # функция, возвращающая словарь с частотой встречаемости каждого символа в строке
    chars_in_percent = {}
    for char, value in dict_chars.items():
        chars_in_percent[char] = round(value / sum(dict_chars.values()) * 100, 5)
    return chars_in_percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
# print(reformat_in_percent(get_count_char(main_str)))
