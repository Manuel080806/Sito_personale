lista = ["La guerra dei mondi", "Viaggio al centro della terra", "Signore degli anelli", "La spada della veritÃ "]
libro_da_prendere = input("Quale libro vuoi prendere in prestito? ")
libri_prestito = []

if libro_da_prendere in lista:
    data_di_acquisto = input("Inserisci la data di oggi (formato dd/MM/yyyy): ")
    giorno, mese, anno = data_di_acquisto.split('/')
    fine_mese = str(int(mese) + 1) 
    fine = giorno + '/' + fine_mese + '/' + anno

    libro = {
        "titolo": libro_da_prendere,
        "data_inizio": data_di_acquisto,
        "data_fine": fine 
    }
    libri_prestito.append(libro)
    print("Libro prenotato con successo")
else:
    print("Il libro che cerchi non Ã¨ presente nella biblioteca")

