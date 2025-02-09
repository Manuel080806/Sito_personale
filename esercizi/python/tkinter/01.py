import tkinter as tk
import random

def DrawCircleByCentre(canvas:tk.Canvas, x, y, radius, **kwargs):
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, **kwargs)


def drawRecursive(canvas, maxLevel, x, y, radius, currentLevel=1, **kwargs):
    mycolor = randColor()
    DrawCircleByCentre(canvas, x, y, radius, fill=mycolor, **kwargs)
    if currentLevel < maxLevel:
        drawRecursive(canvas, maxLevel, x-radius*0.59, y, radius*0.42, currentLevel=currentLevel+1, **kwargs)
        drawRecursive(canvas, maxLevel, x+radius*0.59, y, radius*0.42, currentLevel=currentLevel+1, **kwargs)
        drawRecursive(canvas, maxLevel, x, y-radius*0.59, radius*0.42, currentLevel=currentLevel+1, **kwargs)
        drawRecursive(canvas, maxLevel, x, y+radius*0.59, radius*0.42, currentLevel=currentLevel+1, **kwargs)


def randColor():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color = '#'
    for i in range(6):
        color += random.choice(digits)
    return color


window = tk.Tk()
canvas = tk.Canvas(height=700, width=700, highlightthickness=0, borderwidth=0)
canvas.pack()
drawRecursive(canvas, 7, 350, 350, 350)
window.mainloop()