import tkinter

window=tkinter.Tk()

window.title("그림판")
window.geometry("640x400+100+100")
window.resizable(False, False)

canvas = tkinter.Canvas(window, width = 500, height = 230, relief = "solid", bd = 1)
canvas.pack(side = "top")
canvas.place(x = 70, y = 10)

#색 변경 버튼(예시)
button1 = tkinter.Button(relief = "solid", width = 20, text = "red").place(height = 30, x = 260, y = 247)       
button2 = tkinter.Button(relief = "solid", width = 20, text = "blue").place(height = 30, x = 260, y = 278)       
button3 = tkinter.Button(relief = "solid", width = 20, text = "black").place(height = 30, x = 260, y = 309)       
button4 = tkinter.Button(relief = "solid", width = 20, text = "white").place(height = 30, x = 260, y = 340)       


window.mainloop()
