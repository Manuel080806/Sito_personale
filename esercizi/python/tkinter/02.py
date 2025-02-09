import tkinter
# Uso di entry e label. Inoltre c'ÃƒÂ¨ la gestione di click centro e dx su bottone

window = tkinter.Tk()
window.title("GUI ENTRY")

def dollariEuro():
    num=float(campoTesto.get())
    num=num*0.89
    etichetta['text'] = num

def euroDollari():
    num=float(campoTesto.get())
    num=num/0.89
    etichetta['text'] = num

btn1 = tkinter.Button(window, text = "Dollari-Euro", command = dollariEuro)
btn1.pack()
btn2 = tkinter.Button(window, text = "Euro-Dollari", command = euroDollari)
btn2.pack()

campoTesto = tkinter.Entry(window)
campoTesto.insert(0, 'scrivi qui')
campoTesto.pack()

etichetta = tkinter.Label(window, text = 'testo etichetta')
etichetta.pack()

window.mainloop()