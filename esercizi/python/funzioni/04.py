from random import randint


def eseguiLanci(n):
  lanci = []
  for _ in range(n):
    lanci.append(randint(0, 36))
  return lanci


def verificaNumero(lista, num):
  if num in lista:
    return True
  return False

def verificaCompreso(lista):
  for i in range(len(lista)):
    if lista[i]>=5 and lista[i]<=9 in lista:
        return True
  return False

def verificaDispari(lista):
  for i in range(len(lista)):
    if lista[i]%2==0 in lista:
        return False
  return True

def verificaZero(lista):
  if 0 not in lista:
    return True
  return False


def simulaLanci(numSimulazioni, numLanci):
  conta_num = 0
  conta_compreso = 0
  conta_dispari = 0
  conta_zero = 0

  for _ in range(numSimulazioni):
    lanci = eseguiLanci(numLanci)

    conta_num += int(verificaNumero(lanci, 13)) 
    conta_compreso += int(verificaCompreso(lanci)) 
    conta_dispari += int(verificaDispari(lanci)) 
    conta_zero += int(verificaZero(lanci))
    
  return conta_num / numSimulazioni * 100, conta_compreso / numSimulazioni * 100, conta_dispari / numSimulazioni * 100, conta_zero/ numSimulazioni * 100  #crea una tupla temporanea


n = int(input("quante simulazioni "))
a, b, c, d = simulaLanci(n, 4) 

print("frequenza che esca 13", a)
print("frequenza che esca un numero compreso tra 5 e 9 inclusi", b)
print("frequenza che in ogni lancio esca un numero dispari", c)
print("frequenza che non esca mai lo zero", d)