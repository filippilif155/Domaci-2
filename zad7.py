#FUNKCIJE ZA PROVJERAVANJE
def provjera_naziva(string):
    validnost = 1
    if len(string) < 2 or len(string) > 50:
        validnost = 0
    return validnost
def provjera_ocjene(string):
    validnost = 1
    try:
        float(string)
    except ValueError:
        validnost = 0
        return validnost
    if float(string) > 10 or float(string) < 0:
        validnost = 0
    return validnost
def provjera_godine(string):
    validnost = 1
    try:
        int(string)
    except ValueError:
        validnost = 0
        return validnost
    if int(string) < 1950 or int(string) > 2019:
        validnost = 0
    return validnost
def provjera_izdavaca(string):
    validnost = 1
    if len(string) < 2 or len(string) > 40:
        validnost = 0
    return validnost
def provjera_zanra(string):
    validnost = 1
    lista_upisanih_zanrova = string.split()
    if len(lista_upisanih_zanrova) > 3:
        validnost = 0
        return validnost
    for elem in lista_upisanih_zanrova:
        validnost = 0
        k = 0
        for dati_zanr in lista_zanrova:
            if dati_zanr == elem:
                validnost = 1
                break
            k += 1
        if k == len(lista_zanrova) and validnost == 0:
            break
    return validnost
#Global za date zanrove kako bi mogli koristiti u bilo kom dijelu koda a potrebna je vise puta
global lista_zanrova
lista_zanrova = ['Action', 'Crime','Adventure', 'Sci-Fi','Drama']
#CITANJE POCETNOG FAJLA
with open("igrice.txt", "r") as file:
    string = file.read()
file.close()    
lista_igrice = string.split("\n")
lista_ispravne_igrice = []
#PROVJERA IGRICA ZA POCETNI FAJL
for elem in lista_igrice:
    pomocna_lista = elem.split(';')
    if len(pomocna_lista) != 5:
        continue
    if provjera_naziva(pomocna_lista[0]) != 1:
        continue
    if provjera_ocjene(pomocna_lista[1]) != 1:
        continue
    if provjera_godine(pomocna_lista[2]) != 1:
        continue
    if provjera_izdavaca(pomocna_lista[3]) != 1:
        continue
    if provjera_zanra(pomocna_lista[4]) != 1:
        continue
    pomocna_lista[4] = pomocna_lista[4].lower()
    lista_ispravne_igrice.append(pomocna_lista)
print("LISTA ISPRAVNE",lista_ispravne_igrice)
#UPIS ISPRAVNO UNESENIH IGRICA U NOVI FAJL 
f = open("igrice1.txt", "w+")
for elem in lista_ispravne_igrice:
    f.write(str(elem))
    f.write('\n')
f.close()
#NOVI UNOS(I)
novi_unos = input("Da li zelite da unesete nove igrice? y/n \n")
while novi_unos == 'y':
    naziv = input('Unesite naziv (ne manje od 2 i vece 50 karaktera):\n')
    if provjera_naziva(naziv) == 0:
        print('Pogresan unos!')
        continue
    while (1):
        ocjena = input('Unesite ocjenu (broj sa decimalnom tackom izmedju 0 i 10): \n')
        if provjera_ocjene(ocjena) == 0:
            print('Pogresan unos!')
            continue
        break
    while (1):
        godina = input('Unesite godinu izdavanja igrice (ne manje od 1950 i vece od tekuce godine):\n')
        if provjera_godine(godina) == 0:
            print('Pogresan unos!')
            continue
        else:
            break
    while (1):
        autor = input('Unesite izadavaca igrice (ne manje od 2 i vece od 40 karaktera):\n')
        if provjera_izdavaca(autor) == 0:
            print('Pogresan unos!')
            continue
        else:
            break
    while (1):
        zanr = input(f'Unesite neki od datih zanrova {lista_zanrova}\nUkoliko unosite vise zanrova (do 3) razdvojite ih space-om:\n ')
        if provjera_zanra(zanr) == 0:
            print('Pogresan unos!')
            continue
        else:
            break
    prelazna_lista = [naziv, ocjena, godina, autor, zanr]
    lista_ispravne_igrice.append(prelazna_lista)
    f = open("igrice1.txt", "a")    
    f.write(str(prelazna_lista))    #Upisivanje u novi fajl
    f.close()
    novi_unos = input("Da li zelite da unesete nove igrice? y/n \n")
#DICTIONARY ISPIS U TERMINALU 
lista_igara = []
for elem in lista_ispravne_igrice:
    prelazni_dict = {}
    elem_prel = list(elem)
    prelazni_dict.update({'Naziv': elem_prel[0]})
    prelazni_dict.update({'Ocjena': float(elem_prel[1])})
    prelazni_dict.update({'Godina': int(elem_prel[2])})
    prelazni_dict.update({'Izdavac': elem_prel[3]})
    prelazni_dict.update({'Zanr': list(elem_prel[4].split())})
    lista_igara.append(prelazni_dict)
print(lista_igara)
#FILTRIRANJE
filtriranje = input('Da li zelite da filtrirate listu? y/n \n')
while filtriranje == 'y':
    lista = []
    filtriranje = input("Da li zelite da filtrirate listu po nazivu (N), ocjeni (O), godini (G), izdavacu (I) ili zanru (Z)?\n ")
    if filtriranje == 'N':
        term = input('Ukucajte term sa kojim pocinje igrica:\n')
        lista = [[ime, ocjena, godina, izdavac, zanr] for (ime, ocjena, godina, izdavac, zanr)  in lista_ispravne_igrice if ime.startswith(term)]
    elif filtriranje == 'O':
        ocjena_up = input("Unesite ocjenu i prikazace se igrice sa vecom ocjenom od zadate:\n")
        if provjera_ocjene(ocjena_up) == 1:
            lista = [[ime, ocjena, godina, izdavac, zanr] for (ime, ocjena, godina, izdavac, zanr)  in lista_ispravne_igrice if float(ocjena)>= float(ocjena_up)]
        else:
            print('Pogresno unijeta ocjena!')
    elif filtriranje == 'G':
        while (1):
            kako = input("Zelite li da pretrazite igrice prije ili nakon odredjene godine? p/n:\n")
            if kako != 'p' and kako != 'n':
                print('Pogresan unos!')
                continue
            else:
                break
        god = input("Unesite godinu:\n")
        if provjera_godine(god) == 1:
            if kako == 'n':
                lista = [[ime, ocjena, godina, izdavac, zanr] for (ime, ocjena, godina, izdavac, zanr)  in lista_ispravne_igrice if int(godina) >= int(god)]
                #Jednostavnije i citljivije je koristiti filter, medjutim, htio sam da predjem i list comprehension u nekom od zadataka. U svakom filtriranju bi se mogla...
                #...iskoristiti filter funkcija u slicnom obliku kao u liniji 161, medjutim za zanr bi bilo malo komplikovanije, pa je jednostavnije kako je i napisano (liniji 171)
                #lista = list(filter(lambda x: int(x[2]) >= god ,lista_ispravne_igrice))
            else:
                lista = [[ime, ocjena, godina, izdavac, zanr] for (ime, ocjena, godina, izdavac, zanr)  in lista_ispravne_igrice if int(godina) <= int(god)]
        else:
            print("Pogresan unos!")
    elif filtriranje == 'I':
        term = input('Ukucajte term sa kojim pocinje igrica:\n')
        lista = [[ime, ocjena, godina, izdavac, zanr] for (ime, ocjena, godina, izdavac, zanr)  in lista_ispravne_igrice if izdavac.startswith(term)]
    elif filtriranje == 'Z':
        zan = input(f"Unesite jedan ili vise zanrova {lista_zanrova}\nVise zanrova odvojite space-om:\n")
        if provjera_zanra(zan) == 1:
            zan = zan.lower()
            pomocna_lis = zan.split()
            if len(pomocna_lis) == 1:
                for elem in lista_ispravne_igrice:
                    for elem1 in elem[4].split():
                        if zan == elem1:
                            lista.append(elem)
            elif len(pomocna_lis) == 2:
                for elem in lista_ispravne_igrice:
                    k = 0
                    for elem1 in elem[4].split():
                        if elem1 == pomocna_lis[0]:
                            k += 1
                        elif elem1 == pomocna_lis[1]:
                            k += 1
                    if k == 2:
                        lista.append(elem)
            else:
                lista = [[ime, ocjena, godina, izdavac, zanr] for (ime, ocjena, godina, izdavac, zanr)  in lista_ispravne_igrice if zanr == zan]
        else:
            print('Pogresan unos!')
    else:
        print('Pogresan Unos!')
        filtriranje = input('Da li zelite da filtrirate listu? y/n:\n')
        continue
    lista_igara = []
    for elem in lista:
        prelazni_dict = {}
        elem_prel = list(elem)
        prelazni_dict.update({'Naziv': elem_prel[0]})
        prelazni_dict.update({'Ocjena': float(elem_prel[1])})
        prelazni_dict.update({'Godina': int(elem_prel[2])})
        prelazni_dict.update({'Izdavac': elem_prel[3]})
        prelazni_dict.update({'Zanr': list(elem_prel[4].split())})
        lista_igara.append(prelazni_dict)
    print(lista_igara)
    filtriranje = input('Da li zelite da filtrirate listu? y/n:\n')
                   