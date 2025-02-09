ALG = 1
import datetime

import random
n = int(input("quanti numeri vuoi generare?"))
lista = []
for _ in range(n):
  lista.append(random.randint(1,1000))

date1 = datetime.datetime.now()
if ALG==1:

  for i in range(len(lista)-1):
    i_min = i
    for j in range(i+1,len(lista)):
      if(lista[i] > lista [j]):
        i_min = j
    lista[i], lista[i_min] = lista[i_min], lista[i]
if ALG==2:
  
  vai = True
  iterazoni_esterne=1
  while(vai):
    
    vai=False
    for i in range(len(lista)-iterazoni_esterne):
      if(lista[i] > lista [i+1]):
        lista[i], lista[i+1] = lista[i+1], lista[i]
        vai = True
    iterazoni_esterne+=1
        
diff = datetime.datetime.now() - date1
print("La lista ordinata ",lista)
print("FINE (sec",diff.seconds ,")")