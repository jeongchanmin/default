import tkinter
from tkinter import *
from tkinter import ttk

window=tkinter.Tk()

window.title("그림판")
window.geometry("640x400+100+100")
window.resizable(False, False)

canvas = tkinter.Canvas(window, width = 500, height = 230, relief = "solid", bd = 1)
canvas.pack(side = "top")
canvas.place(x = 70, y = 10)

button1 = tkinter.Button().pack()       #빨간색
button2 = tkinter.Button().pack()       #파란색
button3 = tkinter.Button().pack()       #검정색
button4 = tkinter.Button().pack()       #흰색


window.mainloop()
