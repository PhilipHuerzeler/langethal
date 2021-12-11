from Beverage import *
from datetime import datetime


def calculate_coffein(name):
    if name == "cappucino":
        return Beverage.ESRPESSO.value
    elif name == "doppio":
        return 2*Beverage.ESRPESSO.value
    else:
        return 80

def calculate_Volume(weight, height):
    return 51.44*weight / height + 15.3

def calculate_Time():
    now = datetime.now()
    return now