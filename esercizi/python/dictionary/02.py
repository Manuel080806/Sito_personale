n = int(input("Quanti numeri vuoi inserire? "))
vet = []

while len(vet)<n:

    num = input("inserisci un numero ")
    if num.isnumeric():
        num = int(num)
        if num>=0 and num<1000:
            vet.append(num)
        else:
            print("valore non valido")
    else:
        print("inserisci un valore numerico intero")


dec = [0]*100   

for x in vet:   
    decade = x//10
    dec[decade] += 1

print(dec)