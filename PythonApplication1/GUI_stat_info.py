from tkinter import *
from tkinter import ttk
class GUI_stat_info(object):
    """description of class"""
    
    def Assign(self, master, controller):
        self.contr = controller

        self.info_frame = ttk.Labelframe(master, text='Stat description')
        self.text = Text(self.info_frame, width=40, height=10, wrap = 'word')

        self.text.grid(column = 0, row = 0)

        return self.info_frame

    def setText(self, text):
        self.text.delete(1.0, 'end')
        self.text.insert(1.0, text)
       
        
        

