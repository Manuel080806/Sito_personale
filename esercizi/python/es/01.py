#Anna e Lucia si sottopongono ad un test formato da 10 domande (memorizzare la sequenza di
#risposte giuste/sbagliate in una lista), per ognuna delle quali bisogna scegliere fra due risposte.
#Anna, del tutto impreparata, risponde sempre a caso. Lucia sa rispondere con sicurezza a due
#domande su tre e alla rimanente risponde a caso. Qual Ã¨ la probabilitÃ  che la preparazione di Anna
#appaia non inferiore a quella di Lucia? Realizzare un programma per simulare il quiz di Anna e una
#funzione per simulare il quiz di Lucia e stimare la probabilitÃ  del problema.

import random

risposte = ['G', 'S', 'G', 'S', 'G', 'S', 'G', 'S', 'G', 'S']

ris_esatte_lucia = 0
for i in range(len(risposte)):
  if i % 3 == 0 or i % 3 == 1:
    if risposte[i] == 'G':
      ris_esatte_lucia += 1
  else:
    if random.choice(['G', 'S']) == 'G':
      ris_esatte_lucia += 1

ris_esatte_anna = 0
for i in range(len(risposte)):
  if random.choice(['G', 'S']) == 'G':
    ris_esatte_anna += 1

if ris_esatte_anna >= ris_esatte_lucia:
  print("La preparazione di Anna non Ã¨ inferiore a quella di Lucia")
else:
  print("La preparazione di Anna Ã¨ inferiore a quella di Lucia")

num_simulazioni = 100000
casi_favorevoli = 0
for i in range(num_simulazioni):
  ris_esatte_anna = 0
  ris_esatte_lucia = 0
  for i in range(len(risposte)):
    if i % 3 == 0 or i % 3 == 1:
      if risposte[i] == 'G':
        ris_esatte_lucia += 1
    else:
      if random.choice(['G', 'S']) == 'G':
        ris_esatte_lucia += 1
    if random.choice(['G', 'S']) == 'G':
      ris_esatte_anna += 1
  if ris_esatte_anna >= ris_esatte_lucia:
    casi_favorevoli += 1

probabilita = casi_favorevoli / num_simulazioni
print("La probabilitÃ  che la preparazione di Anna sia non inferiore a quella di Lucia Ã¨:", probabilita)