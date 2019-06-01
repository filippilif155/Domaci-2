city_temp_c = [("Podgorica", 20), ("Niksic", 15), ("Budva", 18), ("Cetinje", 16), ("Bijelo Polje", 11), ("Pljevlja", 12)]
city_temp_f = map(lambda elem: (elem[0], (9 / 5) * elem[1] + 32), city_temp_c)
print(list(city_temp_f))
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
print("asdasdasdasa")
print(map_prim(lambda elem: (elem[0], (9 / 5) * elem[1] + 32), city_temp_c))
a = "asAAAawfs"
print(map_prim(lambda x: x.upper(), a))
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

l = list(range(10))
print(filter_prim(lambda num: num % 2 == 0,l))
l = "asdASdasdD"
print(filter_prim(lambda x: x.islower(), l))