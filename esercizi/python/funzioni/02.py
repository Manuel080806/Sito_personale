import random

def tiro(tipo=1):

    perc = random.randint(1,10)     #estrae da 1 a 10 compreso
    match tipo:
        case 1:
            if perc < 10:
                return tipo
        case 2:
            if perc < 6:
                return tipo
        case 3:
            if perc < 4:
                return tipo    
    return 0                  

def turnoGiocatore(listaTiri, automatico=False):      
    if not automatico:
        tipo = int(input("quale tipo di tiro vuoi fare? "))
    else:
        tipo = random.randint(1,3)
    listaTiri.append(tiro(tipo))
    return listaTiri[-1]      

auto = False
r = input("vuoi giocare in automatico? (s/n) ")
if "s" in r.lower():
    auto = True

giocatore1 = input("inserisci il nome del primo giocatore ")
giocatore2 = input("inserisci il nome del secondo giocatore ")
lista1 = []
lista2 = []
for i in range(10):
    turnoGiocatore(lista1, auto)
    turnoGiocatore(lista2, auto)


print("il giocatore", giocatore1, "ha realizzato", sum(lista1), "punti")
print("il giocatore", giocatore2, "ha realizzato", sum(lista2), "punti")