import tkinter as tk
from random import randint, choice

root = tk.Tk()
root.title("Griglia")
matrice = []
n=4

def scelta_casella_vincente(griglia):
    indice = randint(0, len(griglia)-1)
    griglia[indice]["btn"].config(command=vincente)
    return griglia[indice]

def sbagliato():
    label["text"] = "hai perso"

def vincente():
    label["text"] = "hai vinto"

def elimina_bg():
    for i in range(len(matrice)):
        if matrice[i]["bg"] != casella_vincente["bg"]:
            matrice[i]["btn"].config(bg="grey", state="disable")

def elimina_fg():
    for i in range(len(matrice)):
        if matrice[i]["fg"] != casella_vincente["fg"]:
            matrice[i]["btn"].config(fg="white", state="disable")

def elimina_pari_dispari():
    for i in range(len(matrice)):
        if matrice[i]["txt"]%2 != casella_vincente["txt"]%2:
            matrice[i]["btn"].config(text="sbagliata", state="disable")

def crea_griglia(n, griglia):
    bg_color = ["green", "red"]
    fg_color = ["yellow", "blue"]
    for i in range(n):
        for j in range(n):
            bg = choice(bg_color)
            fg = choice(fg_color)
            txt = randint(1,6)
            btn = tk.Button(root, width=16, height=5, bg=bg, fg=fg, text=txt, font=("Arial", 12, "bold"), command=sbagliato)
            btn.grid(row=i, column=j)
            casella = {"btn":btn, "bg":bg, "fg":fg, "txt":txt}
            griglia.append(casella)

crea_griglia(n, matrice)
casella_vincente = scelta_casella_vincente(matrice)

btn_del_bg = tk.Button(root, text="Elimina il colore di sfondo errato", command=elimina_bg)
btn_del_bg.grid(row=n+1, column=0)
btn_del_fg = tk.Button(root, text="Elimina il colore del testo errato", command=elimina_fg)
btn_del_fg.grid(row=n+1, column=1)
btn_pari_disp = tk.Button(root, text="Elimina pari o dispari", command=elimina_pari_dispari)
btn_pari_disp.grid(row=n+1, column=2)

label = tk.Label(root)
label.grid(row=n+1, column=3)
root.mainloop()