from tkinter import *
from tkinter import ttk
class GroupLayoutDemo(object):
    """description of class"""

    def __init__(self, master):
        self.paneeli = ttk.Frame(master)
        self.labelit = []
        self.vetovalikot = []
        self.ok = ttk.Button(self.paneeli)
        self.cancel = ttk.Button(self.paneeli)

        
        
    def asettele(self):
        labelitX = ttk.Panedwindow(self.paneeli, orient=HORIZONTAL)

        for i in range(0,5):
            self.labelit.append(ttk.Label(labelitX, text="Valinta" + i+1))
            self.labelit[i].grid(column = i)

        self.paneeli.grid(column=0, row = 0)
        labelitX.grid(column=0, row = 0)
    


