def flo(broj):
    val_str = 1
    pom_lis = broj.split(".")
    if len(pom_lis) != 2:
        val_str = 0
        return val_str
    for i in pom_lis:
        if i.isnumeric() != True:
            val_str = 0
            break
    return val_str
def bro(str1):
    val = 1
    for i in str1:
        print(type(i))
        if i.isnumeric() != True:
            val = 0
    return val

        
def provjera_unosa(list):
    validnost = 1
    k = 0
    for elem in list[k]:
        print(list[k])
        list2 = elem.split()
        print(list2)
        if list2[0].isalpha() != True and list2[0].isupper() != True:
            print("0")
            validnost = 0
            break
        elif bro(list2[1]) != 1:
            print(list2[1])
            validnost = 0
            break
        elif flo(list2[2]) != 1:
            print("2")
            validnost = 0
            break
        elif list2[3] != "B" and list2[3] != "S":
            print("3")
            validnost = 0
            break
        if validnost == 0:
            break
        k += 1
    return validnost

from functools import reduce
def rezultat(list):
    buy = float(reduce(lambda x, y: float(x[2]) + float(b[2]),list(filter(lambda x: x[3] == "B", list))))
    sell = float(reduce(lambda x, y: float(x[2]) + float(b[2]),list(filter(lambda x: x[3] == "S", list))))
    a = "Buy : " + str(buy) + "Sell : " + str(sell)
    return a
izlaz = 0
lista = []
lista1 = []
while(1):
    str = input("Unesite vrijednosti u datom obliku:\n NAZIV (samo velika slova) (razmak) BROJ AKCIJA (prirodan broj) (razmak) CIJENA (broj u dacimalnom zapisu) (razmak) STATUS (B ili S))\nVise podataka mozete unijeti tako sto datu semu unosa odvojite zarezom i u istom obliku unosite sledece podatke\n Kada unesete podatke pritisnite Enter\n \tUNOS PODATAKA:\n ")
    lista2 = (str.split(","))
    for i in lista2:
        lista.append(lista2)
        print(lista)
    if provjera_unosa(lista) == 1:
        lista1 = lista + lista1
        print(rezultat(list))
        i =  input("Ako zelite da unesete jos podataka ukucajte y")
        if i == "y":
            continue
        else:
            break
    break
    '''else:
        print("NEVALIDAN UNOS!")
        izlaz += 1
        if i == 3:
            break
        continue'''
a = '123123'
print(a.isnumeric())