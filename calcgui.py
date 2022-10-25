from tkinter import *
from tkinter import ttk
from utils import math_functions

root = Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()
'''
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text=f"3+3 = {math_functions.add(3, 3)}").grid(column=0, row=1)
'''


root.mainloop()