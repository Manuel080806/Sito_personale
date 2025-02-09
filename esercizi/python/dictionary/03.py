n = int(input("Quanti numeri vuoi inserire? "))
lista1 = []

while len(lista1)<n:
    lista1.append(int(input("inserisci un numero ")))

massimo = max(lista1)
minimo = min(lista1)

if minimo<0:
    minimo = minimo*(-1)
if massimo<0:
    massimo = massimo*(-1)

if massimo>minimo:
    valore_assoluto = massimo
else:
    valore_assoluto = minimo

for x in range(n):
    lista1[x] = lista1[x]/valore_assoluto

print(lista1)