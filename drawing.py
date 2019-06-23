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

button1 = tkinter.Button(relief = "solid", width = 20, text = "red").place(height = 30, x = 260, y = 247)        #빨간색
button2 = tkinter.Button(relief = "solid", width = 20, text = "blue").place(height = 30, x = 260, y = 278)       #파란색
button3 = tkinter.Button(relief = "solid", width = 20, text = "black").place(height = 30, x = 260, y = 309)       #검정색
button4 = tkinter.Button(relief = "solid", width = 20, text = "white").place(height = 30, x = 260, y = 340)       #흰색


window.mainloop()
