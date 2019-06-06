         #MAP
def map_prim(funct, podatak):
    lista = []
    for i in podatak:
        lista.append(funct(i))
    if type(podatak) is str:
        return(''.join(lista))
    elif type(podatak) is set:
        return(set(lista))
    elif type(podatak) is tuple:
        return(tuple(lista))
    else:
        return lista
'''
city_temp_c = [("Podgorica", 20), ("Niksic", 15), ("Budva", 18), ("Cetinje", 16), ("Bijelo Polje", 11), ("Pljevlja", 12)]
city_temp_f = map(lambda elem: (elem[0], (9 / 5) * elem[1] + 32), city_temp_c)
print(map_prim(lambda elem: (elem[0], (9 / 5) * elem[1] + 32), city_temp_c))
a = "asAAAawfs"
print(map_prim(lambda x: x.upper(), a))
'''
        #FILTER
def filter_prim(funct, podatak):
    lista = []
    for i in podatak:
        if funct(i) == True:
            lista.append(i)
    if type(podatak) is str:
        return(''.join(lista))
    elif type(podatak) is set:
        return(set(lista))
    elif type(podatak) is tuple:
        return(tuple(lista))
    else:
        return lista
'''
l = list(range(10))
print(filter_prim(lambda num: num % 2 == 0,l))
l = "asdASdasdD"
print(filter_prim(lambda x: x.islower(), l))
'''
         #REDUCE
def reduce_prim(funct, podatak):
    rez = funct(podatak[0], podatak[1])
    i = 2
    while i != len(podatak):
        rez = funct(rez,podatak[i])
        i += 1
    return rez
'''
print(reduce_prim(lambda x, y: x+y,[1,2,3,4]))
print(reduce_prim(lambda a,b : a if a > b else b,[1,2,3,4]))
'''