string = 'qweqrty'
char = ''
symb_index = []

for symb in string:
    if symb in char:
        symb_index.append(string.index(symb) + 1)
        continue
    else:
        char += symb

if len(string[symb_index[0]:]) > len(string[:symb_index[0]]):
    print(len(string[symb_index[0]:]))
else:
    print(len(string[:symb_index[0]]))
