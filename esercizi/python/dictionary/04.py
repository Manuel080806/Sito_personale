lista = []

r='s'
while r=='s':
    lista.append(str(input("Inserisci una stringa nella lista ")))

    r=input("Vuoi inserire un altra stringa nella lista? (s/n) ")

lista2 = [len(t) for t in lista]

print()
print(lista)
print()
print(lista2)