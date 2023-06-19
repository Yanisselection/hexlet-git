# Протокол итерации - один из важнейших протоколов, который позволяет проходить по каждому элементу в коллекции
# Создаем переменную и вкладываем в неё iter(Входящая коллекция) 
# next(переменная в которую вложена iter)

   l = [1, 2, 3, 4, 5]
    variable_iterbl = iter(l)
    next(variable_iterbl)
    >>> 1
    next(variable_iterbl)
    >>> 2
    ...



# Циклы в итераторах, здесь при каждом вызове будет вызываться новая итерация до выполнения условия

    l = ['1', '22', '333', '4444', '55555', '666666', '7777777', '88888888', '999999999']
    
    def search_long_string(numbers):
        for item in numbers:
            if len(item) >= 5:
                return item
    

# Для успешного прохождения итерации с запоминанием позиции (курсора) используем iter()

    iter_var = iter(l)
    search_long_string(iter_var)
    >>> 55555
    search_long_string(iter_var)
    >>> 666666
    ...



# Генераторы iterbl элементы, которые не хранятся, а создаются по мере необходимости
# range - перезапускаемый генератор, такой итератор можно вызывать сколько угодно раз, потому что значения генерируются заново 

    numbers = range(10)
    for n in numbers:
            print(n)

    0
    1
    2
    3
    4
    ...


# Не перезапускаемые генераторы, по значениям такого генератора можно пройти один раз (next()):

    l = enumerate('qwerty')
    list(l)
    [(0,'q'), (1,'w'), (2, 'e')...(5, 'y')]


# Встроенный итератор zip:

    keys = ['one', 'two', 'three']
    values = [1, 2, 3, 4]
    for k,v in zip(keys,values):
        print(k, '=', v)
    
    one = 1
    two = 2
    three = 3




    z = zip(range(5),'12345',[True, False, True, False])
    list(z)
    [(0,'1',True),(1,'2',False),...(3,'4',False)]
    list(z)
    []



# Zip перестает генерировать кортежи, как только заканчиваются элементы в любом из источников 

# Задача по поиску совпадения минуя первый индекс 

    def find_second_index(key, string):
        coincidences = []
        for (index, item) in enumerate(string):
            if key == item:
                coincidences.append(index)

        if len(coincidences) < 2:
            return None
        return coincidences[1]


    print(find_second_index('a', 'cata'))























