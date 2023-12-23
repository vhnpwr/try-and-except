from tkinter import *
root=Tk()

root.title("bad geometry")
try:
    root.geometry("400")
    
except:
    print("bad geometry error")

root.mainloop()
