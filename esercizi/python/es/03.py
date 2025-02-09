lista=[]
i=1
while i<=3:
    print("Inserisci i dati per la concorente numero",i)
    concorente={}
    concorente['Nome']=str(input('inserisci il Nome: '))
    concorente['Cognome']=str(input('inserisci il Cognome: '))
    concorente['Percentuale']=int(input('inserisci la Percentuale: '))
    i+=1
    lista.append(concorente)

max_Percentuale = 0
Percentuale = None
for concorente in lista:
    if concorente['Percentuale'] > max_Percentuale:
        max_Percentuale = concorente['Percentuale']
        Percentuale = concorente['Nome']

print("il concorente che ha fatto la percentuale maggiore Ã¨:", Percentuale)