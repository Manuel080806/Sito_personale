import datetime
persona = {}
persona['Nome'] = input("Inserisci il nome ")
persona["Cognome"] = input("Inserisci il cognome ")
persona["DataNascita"] = input("Inserisci la data di nascita (yyyy/MM/dd) ")
persona["LuogoNascita"] = input("Inserisci il luogo di nascita ")
persona["CittaResidenza"] = input("Inserisci la citta' di residenza ")

#calcolo l'eta'
annoNascita = int(persona["DataNascita"][0:4])
meseNascita = int(persona["DataNascita"][5:7])
giornoNascita = int(persona["DataNascita"][8:10])
annoCorrente = datetime.date.today().year
print ("l'eta' e'", annoCorrente-annoNascita)

cf = ""
vocali = "aeiouAEIOU"

for c in persona["Cognome"]:
    if c not in vocali:
        cf += c
        if len(cf)==3:
            break
for c in persona["Nome"]:
    if c not in vocali:
        cf += c
        if len(cf)==6:
            break
        

cf += str(annoNascita%100)
car_mese = 'ABCDEHLMPRST'
cf += car_mese[meseNascita-1]

tmp = str(giornoNascita)
if len(tmp)==1:
    tmp= '0'+tmp
cf += tmp

print(cf)