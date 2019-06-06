def get_tag_content(kod, tag, broj_oz, brojac, pocetak):
    len_kod = len(kod)
    len_tag = len(tag)
    lista = []
    lista1 = []
    lista_str = []
    while brojac < len_kod:
        provjera = 0
        if kod[brojac] == '<':
            n = 1
            i = 0
            if kod[brojac + n] == '/':
                n += 1
                while   n < len_tag + 2:
                    if kod[brojac + n] != tag[i]:
                        provjera = 1
                        break
                    n += 1
                    i += 1  
                if provjera == 0:
                    lista_str.append((kod[pocetak:brojac].rstrip()).lstrip()) #trazeni string stavljamo u listu
                    broj_oz = broj_oz - 1
                    brojac = brojac + n
                    if broj_oz != 0:
                        break
            elif kod[brojac + n] == tag[i]:
                n += 1
                i += 1
                while  n < len_tag + 1:
                    if kod[brojac + n] != tag[i]:
                        provjera = 1
                        break 
                    
                    n += 1
                    i += 1  
                if provjera == 0:
                    if kod[brojac + n] == '>':
                        broj_oz += 1
                        if broj_oz == 1:
                            pocetak = brojac + n + 1
                            brojac = brojac + n + 1
                        if broj_oz > 1:
                            pocetak1 = brojac + n + 1
                            brojac = brojac + n + 1
                            lista1 = get_tag_content(kod, tag, broj_oz, brojac, pocetak1) # 1 za tag u tagu opet pozivamo f-ju
                            lista_str = lista_str + lista1[0]
                            broj_oz = int(lista1[2])
                            brojac = int(lista1[1])
                            lista1 = []
                    elif kod[brojac + n] == ' ':       
                        n += 1
                        while(1):
                            if kod[brojac + n] == '>':
                                break
                            n += 1
                        broj_oz += 1
                        if broj_oz == 1:
                            pocetak = brojac + n + 1
                            brojac = brojac + n + 1
                        if broj_oz > 1:
                            pocetak1 = brojac + n + 1
                            brojac = broj_oz + n + 1
                            lista1 = get_tag_content(kod, tag, broj_oz, brojac, pocetak1) # 1
                            lista_str = lista_str + lista1[0]
                            brojac = int(lista1[1])
                            broj_oz = int(lista1[2])
        brojac += 1
    lista = [lista_str, brojac, broj_oz]
    return lista
def gettg(kod, tag):                      
    brojac = 0
    pocetak = 0
    broj_oz = 0
    return get_tag_content(kod, tag, brojac, pocetak, broj_oz)[0]


with open('html.txt', 'r') as file:
    kod1 = file.read().replace('\n', '')  
file.close()
#print(kod1)  
tag1 = input("Unesite zeljeni tag :\n")
print(gettg(kod1, tag1))
''' Zadatak mozda zahtijeva "objasnjenje" -- Kako tag u sebi moze sadrzati isti tag dobijamo funkciju koja poziva samu
sebe get_tag_content, dok je funkcija gettg postavljena radi ispunjavanja forme zadate zadatkom... A i zanimljiva mi rekurzija 
bi pa steta da se brise :|'''