lista=[8,5,2,6,9,3,1,4,0,7]
for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if(lista[i] > lista [j]):
            lista[i], lista[j] = lista[j], lista[i]

print(lista)