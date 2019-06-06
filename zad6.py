#PROVJERA UNOSA CIJENE (float)
def flo(broj):
    val_str = 1
    pom_lis = broj.split(".")
    if len(pom_lis) != 2:
        val_str = 0
        return val_str
    for i in pom_lis:
        if i.isnumeric() != True:
            val_str = 0
            return val_str
            break
    return val_str

#PROVJERA NAZIVA AKCIJE
def naziv_akc(stri): 
    validnost = 1
    for i in stri:
        if i == " ":
            validnost = 0
            break
    return validnost

#PROVJERA UNOSA      
def provjera_unosa(lista_un): 
    validnost = 1
    k = 0
    for elem in lista_un:
        privremena_lista = elem.split()
        if len(privremena_lista) == 4:
            if naziv_akc(privremena_lista[0]) != 1:
                validnost = 0
                break
            elif privremena_lista[1].isnumeric() != True:
                validnost = 0
                break
            elif flo(privremena_lista[2]) != 1:
                validnost = 0
                break
            elif privremena_lista[3] != "B" and privremena_lista[3] != "S":
                validnost = 0
                break
        else:
            validnost = 0
            break
        k += 1
    return validnost
    
#RACUNANJE REZULTATA
from functools import reduce
def rezultat(lista):
    buy_pom = list(filter(lambda x: x[3] == "B", lista))
    buy_pom.insert(0, 0.00)                                                          # Unijet float 0.00 kao prvi element liste kako se ne bi pisalo float(x[2]) u redu 49 jer onda dolazi do greske...
    buy = round(float(reduce((lambda x, y: x + float(y[2])*float(y[1])),buy_pom)), 2)#...  kako je f(val) (uzrok reduce funkcija) float pa nema [2] element. Isto vazi i za sell vrijednost(red 52).
    sell_pom = list(filter(lambda x: x[3] == "S", lista))
    sell_pom.insert(0, 0.00)
    sell = round(float(reduce((lambda x, y: x + float(y[2])*float(y[1])),sell_pom)), 2)
    a = "Buy : " + str(buy) + " " + "Sell : " + str(sell)
    return a

#PETLJA UNOSA I REZULTAT
while(1):
    lista_tacnih_unosa = []
    string = input("Unesite vrijednosti u datom obliku:\n NAZIV (samo velika slova) (razmak) BROJ AKCIJA (prirodan broj) (razmak) CIJENA (broj u dacimalnom zapisu) (razmak) STATUS (B ili S))\nVise podataka mozete unijeti tako sto datu semu unosa odvojite zarezom i u istom obliku unosite sledece podatke\n Kada unesete podatke pritisnite Enter\n \tUNOS PODATAKA:\n ")
    lista_unosa = (string.split(","))
    if provjera_unosa(lista_unosa) != 1:
        print ("NEVALIDAN UNOS!")
    else:
        for elem in lista_unosa:
            lista_tacnih_unosa.append(elem.split())
        print(rezultat(lista_tacnih_unosa))
    nov_unos = input("Ukoliko zelite da unesete nove podatake ukucajte Y:\n")
    if nov_unos == "Y":
        continue
    else:
        break
    