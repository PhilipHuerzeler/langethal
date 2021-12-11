from tkinter import *
from GUI import *
from Beverage import *

def calculate_coffein(name):
    if name == "cappucino":
        return Beverage.ESRPESSO.value
    elif name == "doppio":
        return 2*Beverage.ESRPESSO.value

if __name__ == "__main__": 
    window=Tk()
    mywin=MyWindow(window)
    window.title('Hello Python')
    window.geometry("400x300+10+10")
    window.mainloop()
