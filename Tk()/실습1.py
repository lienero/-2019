from tkinter import *
window = Tk()

lbl = Label(window,text="이름")
lbl.pack()

txt = Entry(window)
txt.pack()

btn = Button(window, text="OK")
btn.pack()

window.mainloop()
