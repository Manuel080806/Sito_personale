def ricerca_binaria(val, lista, lenght, i_start=0,):    
    pivot  = i_start + lenght//2    
    if pivot >= len(lista): 
        return -1
    if lista[pivot]==val:
        return pivot
    else:
        if lenght == 1:
            return -1
        else:
            if lista[pivot] < val:
                return ricerca_binaria(val, lista, lenght//2, pivot+1)
            else:
                return ricerca_binaria(val, lista, lenght//2, i_start)


lista=[1,3,4,5,6,8,9,10,13,15,16,18,19,20]
val = int(input("Inserisci il numero intero da cercare: "))
indice = ricerca_binaria(val,lista,len(lista))
print(indice)