#tkinter호출
import tkinter                                                                                                    
from tkinter import *                                                                                             
from tkinter import ttk               

#메인 설정
window=tkinter.Tk()                                                                                                      #창 띄우기

window.title("그림판")                                                                                                   #창 이름
window.geometry("640x400+100+100")                                                                                       #창 크기
window.resizable(False, False)                                                                                           #창 크기 조절가능 여부

#마우스 설정
def draw(event):
  glabal x0, y0
  canvas.create_line(x0, y0, event.x,event.y)
  x0, y0 = event.x ,event.y
  
def down(event):
  global x0, y0
  x0, y0 = event.x, event.y
  
def up(event):
  global x0, y0
  if (x0,y0) == (event.x, event.y):
    canvas.create_line(x0, y0, x0+1, y0+1)

#캔버스 설정
canvas = tkinter.Canvas(window, width = 500, height = 230, relief = "solid", bd = 1)                                  #캔버스 크기, 창의 테두리 
canvas.pack(side = "top")                                                                                             #캔버스 위치
canvas.place(x = 70, y = 10)                                                                                          #캔버스 위치

#버튼 설정
button1 = tkinter.Button(relief = "solid", width = 20, text = "red").place(height = 30, x = 260, y = 247)            #빨간색 펜 버튼
button2 = tkinter.Button(relief = "solid", width = 20, text = "blue").place(height = 30, x = 260, y = 278)           #파란색 펜 버튼
button3 = tkinter.Button(relief = "solid", width = 20, text = "black").place(height = 30, x = 260, y = 309)          #검정색 펜 버튼
button4 = tkinter.Button(relief = "solid", width = 20, text = "white").place(height = 30, x = 260, y = 340)          #흰색 펜 버튼(지우개)

#창 유지
window.mainloop() 
