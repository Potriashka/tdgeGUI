from tkinter import *
from tkinter import ttk  
from tkinter.colorchooser import askcolor 
import main
from tkinter.ttk import Radiobutton
from tkinter import filedialog

def resizable3():
	global resizable2
	resizable2 = True

def color_bg():
	global true
	true = "image"
	global result
	result = askcolor(title = "Choose color")
	print(result[1])

def image_bg():
	global true
	true = "picture"
	global file
	file = filedialog.askopenfilename()

def clicked():
	name = title.get()
	height = hei.get()
	width = wid.get()
	global game
	game = main.Game(movement=True, height=int(height), width=int(width), title=(name))
	txt = Entry(window, width=10)
	if true == "image":
		if resizable3 == True:
			main.display.set_background(game, resizable=True, background_type="color", color=main.hex_to_rgb(result[1]))
		else:
			main.display.set_background(game, background_type="color", color=main.hex_to_rgb(result[1]))
	elif true == "picture":
		main.display.set_background(game, background_type="image", image_path=file)

window = Tk()  
window.title("3D Game Engine")  
window.geometry('400x250')

tab_control = ttk.Notebook(window)  

tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control) 

tab_control.add(tab1, text='Window')  
tab_control.add(tab2, text='Objects') 

name = Label(tab1, text="3D Game Engine", font=("Arial Bold", 30))
name.place(x=50, y=5)

color = Radiobutton(tab1, text='Color bg', value=1, command=color_bg)  
color.place(x=20, y=165)

image = Radiobutton(tab1, text='Picture bg', value=2, command=image_bg) 
image.place(x=20, y=185)

titletext = Label(tab1, text="Project title", font=("Arial Bold", 10))
titletext.place(x=18, y=50)

title = Entry(tab1, width=15)  
title.place(x=10, y=75)

resizable_btn = Radiobutton(tab1, text='Resizible', value=3, command=resizable3) 
resizable_btn.place(x=160, y=60)

wid = Entry(tab1, width=8)  
wid.place(x=12, y=136.5)

widtext = Label(tab1, text="width", font=("Arial Bold", 10))
widtext.place(x=67, y=135)


hei = Entry(tab1, width=8)
hei.place(x=12, y=116.5)

heitext = Label(tab1, text="height", font=("Arial Bold", 10))
heitext.place(x=67, y=115)

btn = Button(tab1, text="Start", command=clicked)  
btn.place(x=160, y=195)

lbl12 = Label(tab1, text="Window size", font=("Arial Bold", 10))
lbl12.place(x=15, y=95)

txt = Entry(tab1, width=10, state='disabled')

tab_control.pack(expand=1, fill='both')

window.mainloop()
