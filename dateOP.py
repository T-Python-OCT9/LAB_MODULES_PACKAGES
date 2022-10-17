## Create a new module and name it "dateOP.py" ,  dateOP has the following:
from datetime import date


## A function that when called prints the current date.
def current_date()-> str:
    print(date.today())