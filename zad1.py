from random import choice
lista = list(range(1,11))
pomocna_lista1 = []
pomocna_lista = list(lista)
brojac = 0
while brojac != 5:
    element = choice(pomocna_lista)
    pomocna_lista1.append(element)
    pomocna_lista.remove(element)
    brojac += 1
konacna_lista = list(zip(pomocna_lista,pomocna_lista1))