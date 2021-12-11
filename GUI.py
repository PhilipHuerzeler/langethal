from tkinter import *
import Calculator

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Weight in kg')
        self.lbl2=Label(win, text='Height in cm')
        self.lbl3=Label(win, text='Volume')
        self.lbl4=Label(win, text='Beverage')
        self.lbl5=Label(win, text='Estimated time')

        self.weight=Entry(bd=3)
        self.height=Entry()
        self.volume=Entry()
        self.beverage=Entry()
        self.time=Entry()

        self.lbl1.place(x=100, y=50)
        self.weight.place(x=200, y=50)

        self.lbl2.place(x=100, y=100)
        self.height.place(x=200, y=100)

        self.lbl4.place(x=100, y=150)
        self.beverage.place(x=200, y=150)

        self.lbl3.place(x=100, y=300)
        self.volume.place(x=200, y=300)

        self.lbl5.place(x=100, y=350)
        self.time.place(x=200, y=350)

        self.b1=Button(win, text='Calculate-Volume')
        self.b1.bind('<Button-1>', self.calcVol)
        self.b1.place(x=100, y=200)
        self.b2=Button(win, text='Calculate-Time')
        self.b2.bind('<Button-1>', self.calcTime)
        self.b2.place(x=250, y=200)
        

    
    def calcVol(self, event):
        self.volume.delete(0, 'end')
        result=Calculator.calculate_Volume(int(self.weight.get()), int(self.height.get()))
        self.volume.insert(END, str(result))

    def calcTime(self, event):
        self.time.delete(0, 'end')
        result=Calculator.calculate_Time()
        self.time.insert(END, str(result))

if __name__ == "__main__": 
    window=Tk()
    mywin=MyWindow(window)
    window.title('Hello Python')
    window.geometry("600x600+10+10")
    window.mainloop()