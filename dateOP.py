'''
Create a new module and name it "dateOP.py" , dateOP has the following:
'''
# A function that when called prints the current date.
from datetime import date


def printDate() -> str:
    print(f"Today is: {date.today()}")
