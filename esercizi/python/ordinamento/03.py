def gestisci_ordinamento(nome, cognome, anno, ord):
    if ord == 0:
     ordina(nome, cognome, anno)
    if ord == 1:
     ordina(cognome, nome, anno)
    if ord == 2:
     ordina(anno, nome, cognome)

def ordina(lista, lista1, lista2):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista [j]):
                lista[i], lista[j] = lista[j], lista[i]
                lista1[i], lista1[j] = lista1[j], lista1[i]
                lista2[i], lista2[j] = lista2[j], lista2[i]


nomi = []
cognomi = []
anni = []

n = int(input("quante persone vuoi inserire?"))

for i in range(n):
    nomi.append(input("inserire nome:"))
    cognomi.append(input("inserire cognome:"))
    anni.append(int(input("inserire anno:")))

gestisci_ordinamento(nomi,cognomi,anni,int(input("per quale parametro vuoi ordinare (0/1/2)")))

for i in range(n):
    print (nomi[i], cognomi[i], anni[i])