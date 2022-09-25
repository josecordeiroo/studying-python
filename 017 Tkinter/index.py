from tkinter import *
from turtle import width

app = Tk()
app.title("Zk Estudos")
app.geometry("500x300")
app.configure(background="#008")

txt1=Label(app, text="Apenas um teste", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=150, height=30)


app.mainloop()