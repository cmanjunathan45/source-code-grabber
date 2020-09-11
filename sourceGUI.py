from tkinter import filedialog,ttk,messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import * 
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser

root=tk.Tk()
root.geometry("600x500")
root.config(bg="#3772A4")
root.title("Source Code Grabber | Manjunathan C")
root.iconphoto(False,tk.PhotoImage(file="icon1.png"))

def grab():
	try:
		lets=e1.get()
		page=requests.get(lets)
		parse=BeautifulSoup(page.content,'html.parser')
		def new():
			root1=tk.Tk()
			root1.config(bg="#3772A4")
			root1.title("HTML WINDOW | Manjunathan C")
			root1.geometry("1400x700")
			root.iconphoto(False,tk.PhotoImage(file="icon1.png"))
			tex=ScrolledText(root1,font=("fontawesome",10,"bold italic"),fg="#FFDA4B",bg="#3772A4",height=40,width=160,borderwidth=5)
			tex.pack()
			tex.insert(tk.END,parse.prettify())
			def save():
       				root1.filename = filedialog.asksaveasfile(mode="w",defaultextension='.html')
        			if root1.filename is None:
            			    return
        			file_save =  str(tex.get(1.0,END))
        			root1.filename.write(file_save)
        			root1.filename.close()
			buttons=Button(root1,text="SAVE",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=save)
			buttons.place(x=540,y=600)

			buttoncl=Button(root1,text="CLEAR",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=lambda: tex.delete("1.0",END))
			buttoncl.place(x=640,y=600)
			
			buttonex=Button(root1,text="EXIT",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=root1.quit)
			buttonex.place(x=740,y=600)

			buttonco=Button(root1,text="CONTACT",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=lambda :webbrowser.open("https://github.com/cmanjunathan45/"))
			buttonco.place(x=640,y=700)


		new()

	except:
		messagebox.showerror("Invalid URL","URL format should be proper\nSimple Ex:-\n'http(or)https://example.com/'")

label1=Label(root,text="Source Code Grabber",bg="#3772A4",fg="#FFDA4B",font=("font awesome",20,"bold italic"))
label1.place(x=140,y=20)

label1=Label(root,text="Enter the site URL you want Source Code",bg="#3772A4",fg="#FFDA4B",font=("font awesome",13,"bold italic"))
label1.place(x=100,y=90)

e1=Entry(root,font=("fontawesome",12,"bold italic"),bg="#FFDA4B",fg="#3772A4",width=50,borderwidth=5)
e1.place(x=15,y=140)

buttonclear=Button(root,text="CLEAR",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=lambda: e1.delete(0,END))
buttonclear.place(x=257,y=240)

buttong=Button(root,text="GRAB",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=grab)
buttong.place(x=260,y=200)

buttone=Button(root,text="EXIT",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=root.quit)
buttone.place(x=265,y=280)

buttonc=Button(root,text="CONTACT",font=("fontawesome",10,"bold italic"),bg="#FFDA4B",fg="#3772A4",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttonc.place(x=246,y=320)

root.mainloop()



