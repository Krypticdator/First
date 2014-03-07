from tkinter import *
from tkinter import ttk
from random import choice
class GUI_per_sub():
    """description of class"""
    def __init__(self, master, filepath, label_text='default', rows=10, var_width=40, controller=object()):
        self.components = {}
        self.valuelist = []
        self.Read_file(filepath, self.valuelist)
        self.rows = rows
        self.contr=controller
        self.contr.datasets[label_text]=self
    
        self.topic=label_text
        self.var = StringVar()
        self.frame = ttk.Frame(master)
        p = ttk.Panedwindow(self.frame, orient=HORIZONTAL)
        label = ttk.Label(p, text=label_text, width = 33)
        var_label = ttk.Label(p, textvariable=self.var, width = var_width)
        self.button_random = ttk.Button(p, text='Random', command=self.random_value)
        self.button_choose = ttk.Button(p, text='Choose..', command=self.choose_value)
        self.var.set('Undecided')

        p.add(label)
        

        self.frame.grid(column = 0, row = 0)
        p.grid(column = 0, row = 0)
        label.grid(column = 0, row = 0, sticky=(W))
        var_label.grid(column = 1, row = 0, sticky=(W))
        self.button_choose.grid(column = 2, row = 0)
        self.button_random.grid(column = 3, row = 0)


    def Read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

    def choose_value(self):
        self.window = Toplevel(self.frame)
        frame = ttk.Labelframe(self.window, text=self.topic)
        radio_elements = {} 

        self.decision = StringVar()

        for Value in self.valuelist:
            radio_elements[Value] = ttk.Radiobutton(frame, text=Value, variable=self.decision, value=Value)
        i=0
        r=0
        for item, value in radio_elements.items():
            value.grid(column = r, row = i, sticky=(W))
            i = i+1
            if i==self.rows:
                r = r+1
                i = 0
        frame.grid(column = 0, row = 0)
        ok = ttk.Button(frame, text='Save', command=self.set_value)
        ok.grid(column = 0, row = self.rows + 1, sticky = (W))
    
    def set_value(self):
        self.var.set(self.decision.get())
        self.window.destroy()

    def random_value(self):
        self.var.set(choice(self.valuelist))

    