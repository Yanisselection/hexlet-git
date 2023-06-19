# Задача:

"""Реализуйте функцию is_continuous_sequence, которая проверяет,
является ли переданная последовательность целых чисел возрастающей
непрерывно (не имеющей пропусков чисел).
Например, последовательность [4, 5, 6, 7] — непрерывная,
а [0, 1, 3] — нет. Последовательность может начинаться
с любого числа. Главное условие - отсутствие пропусков чисел.
Последовательность из одного числа не может считаться возрастающей."""


def is_continuous_sequence(collection):
    if len(collection) <= 1:
        return False

    if len(collection) > 1:
        input_numb = collection[0]

    for item in collection:
        if item == input_numb:
            input_numb += 1
        elif item != input_numb:
            return False
    return True


list_colletiont = [-3, -2, -1]

print(is_continuous_sequence(list_colletiont))
