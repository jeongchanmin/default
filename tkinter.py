import tkinter

window = tkinter.Tk()

window.title("test")
window.geometry("1000x300+10+300")
window.resizable(False, False)

label = tkinter.Label(window, text = "Hello")
label.pack()

window.mainloop()
