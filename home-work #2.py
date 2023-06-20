# Реализация функции, принимающей на вход строку
# и возвращающей длину максимальной последовательности
# из неповторяющихся символов


def find_longest_lenght(string):

    unique = ''
    index_char = []

    if len(index_char) < 1:
        print('String is none')
        return None

# Посимвольная проверка
# Поиск совпадений
# if True, условие добавляет индекс совпадения + 1 (т.к. считает с 0)
# Если символа нет, конкатинирует символ

    for char in string:
        if char in unique:
            index_char.append(string.index(char) + 1)
        else:
            unique += char

# Возвращение самой длинной подстроки

    if len(string[index_char[0]:]) > len(string[:index_char[0]]):
        return len(string[index_char[0]:])
    return len(string[:index_char[0]])


l = 'qweqwer'

print(find_longest_lenght(l))
