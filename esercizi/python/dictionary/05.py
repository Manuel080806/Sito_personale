dquisto={
    "prezzo": 100,
    "descrizione": "casco di Cadel Evans",
    "sconto": 20
}
dquisto["quantitÃƒ "] = int(input("Quanti ne vuoi? "))
prezzo_totale = dquisto["prezzo"]*dquisto["quantitÃƒ "]
prezzo_scontato = dquisto["prezzo"] - (dquisto["prezzo"]/100*dquisto["sconto"])
prezzo_totale_scontato = prezzo_scontato*dquisto["quantitÃƒ "]

print(dquisto)
print()
print("Prezzo totale:",prezzo_totale,"Prezzo scontato:",prezzo_totale_scontato)