import random

def aggiungiDomanda(testo,risposta,lista):
    domanda={
        "testo":testo,
        "risposta":risposta
    }
    lista.append(domanda)


def creaDomande5():
    listaDomande=[]
    testo1="In che anno Cadel ha vinto il tour? "
    risp1=2011
    testo2="In che anno Cadel ha vinto il mondiale? "
    risp2=2009
    testo3="In che anno Cadel ha vinto la coppa del mondo di MTB? "
    risp3=2003
    testo4="In che anno e' nato Cadel? "
    risp4=1977
    testo5="Quanti figli ha Cadel? "
    risp5=2
    aggiungiDomanda(testo1,risp1,listaDomande)  
    aggiungiDomanda(testo2,risp2,listaDomande)
    aggiungiDomanda(testo3,risp3,listaDomande)
    aggiungiDomanda(testo4,risp4,listaDomande)
    aggiungiDomanda(testo5,risp5,listaDomande)
    return listaDomande


def estraiDomanda(domande):
    domanda = random.choice(domande)
    domande.remove(domanda)  
    return domanda



lista = creaDomande5()  
ok = True
for i in range(len(lista)):
    domanda = estraiDomanda(lista)
    r=int(input(domanda["testo"]))
    if r != domanda["risposta"]:
        print("hai sbagliato")
        ok = False
        break

if ok:
    print("Bravo! Hai vinto")