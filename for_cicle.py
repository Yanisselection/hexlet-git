# Циклы For - один из видов работы с коллекцией, его задача перебрать все элементы входной коллекции

# Синтаксис:
    collection = [1,2,3,4,5]
    for element in collection:
        print(element)


# Мы также можем изменить элементы списка внутри коллекции (не создавая новую)

    # Создаем коллекцию
    l = [1, 2, 3, 4, 5]
    # Создаем итеративный обход через индекс елемента (0,2,3...) в списке, где каждому элементу присвоился индекс
    for (index,element) in enumerate(l):
    # Берем индекс элемента и проводим операцию с его значение 
        l[index] = element * 10
    
    # Аналог вышевведенного кода:
    for (index,_) in enumerate(l):
        l[index] += 1

    
    # Преждевременный выход из цикла с помощью конструкции условий (if / else / break / continue)
    for item in l:
        if item > l:
            break
   item
   # Выведет последний итерируемый элемент
   # Если коллекция окажется пустой, то переменная не будет определена — имейте это в виду!
   # Поэтому можно использовать Else для ветки for!!!
   items = [-2, 0, -10, -1]
   for item in items:
       if item > 0:
           break
   else:
       item = None

   
   # Возможность использования continue, если строка начинается с #, то цикл её пропускает:
   lines = [
    'one',
    'two',
    '# three',
    'four'] 
   for line in lines:
       if line[:1] == '#':
           continue
        print(line)

    # Ветку else можно также использовать и в конструкции while как и break и continue:
    tries = 3
    while tries:
        print('>>>', end=' ')
        command = input()
        if not command:
            continue
        if command in ('echo', 'cd', 'help'):
            break
        print("Неизвестная команда")
        tries -= 1
    else:
        print('Много неверных попыток ввода, попробуйте позже')



