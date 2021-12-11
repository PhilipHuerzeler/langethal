from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Weight in kg')
        self.lbl2=Label(win, text='Height in cm')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.btn2=Button(win, text='Calculate')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b2=Button(win, text='Calculate')
        self.b2.bind('<Button-1>', self.calc)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    
    def calc(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=51.44*num1 / num2 + 15.3
        self.t3.insert(END, str(result))

