from tkinter import *
root = Tk()
root.title("Fourth GUI")
NameText= Label(text="Hello My Name is",fg="blue",font=20).grid(row=0,column=0)
NameText= Label(text="Thanawat",fg="green",font=20).grid(row=1,column=1)
NameText= Label(text="Puttipipattanasakul",fg="red",font=20).grid(row=2,column=2)
root.geometry("500x300")
root.mainloop()