from tkinter import *
root=Tk()

root.title("adding two numbers")
root.geometry("400x600")

lbl1=Label(root,text="enter first num")
lbl1.place(relx=0.5,rely=0.5,anchor=CENTER)

showResults=Button(root,text="show results")
showResults.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()