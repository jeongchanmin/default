import tkinter

window=tkinter.Tk()

window.title("그림판")
window.geometry("640x400+100+100")
window.resizable(False, False)

canvas = tkinter.Canvas(window)
canvas.pack()

window.mainloop()
