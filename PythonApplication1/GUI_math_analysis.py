from tkinter import *
from tkinter import ttk
from Fuzion import Fuzion
class GUI_math_analysis(object):
    """description of class"""
    
    def assign(self, controller, master, root):
        self.root = root
        self.contr = controller
        self.frame = ttk.Labelframe(master, text='Analysis')
        lbl_bp = ttk.Label(self.frame, text = "Basepoints")
        lbl_times = ttk.Label(self.frame, text = "Times")
        self.var_bp = StringVar()
        self.var_times = StringVar()
        entry_bp = ttk.Entry(self.frame, textvariable = self.var_bp)
        entry_times = ttk.Entry(self.frame, textvariable = self.var_times)
        button = ttk.Button(self.frame, text='Start', command=self.start_calculation)
        
        #self.progress = 0
        #self.p = ttk.Progressbar(self.frame, orient=HORIZONTAL, length=200, mode='determinate', variable = self.progress)

        self.vars = {}
        self.labels = {}
        self.val_labels = {}

        for i in range(0, 60):
            self.vars[i] = StringVar()

        for i in range(0, 60):
            des = "DV " + str(i)
            self.labels[i] = ttk.Label(self.frame, text = des)
        
        for i in range(0, 60):
            self.val_labels[i] = ttk.Label(self.frame, textvariable = self.vars[i])
        
        self.frame.grid(column = 0, row = 0)
        for i in range(0, 30):
            self.labels[i].grid(column = 0, row = i)

        for i in range(30, 60):
            self.labels[i].grid(column = 2, row = i-30)

        for i in range(0, 30):
            self.val_labels[i].grid(column = 1, row = i)
        for i in range(30, 60):
            self.val_labels[i].grid(column = 3, row = i-30)

        lbl_bp.grid(column = 4, row = 0)
        entry_bp.grid(column = 4, row = 1)
        lbl_times.grid(column = 4, row = 2)
        entry_times.grid(column = 4, row = 3)
        button.grid(column = 4, row = 4)
        #self.p.grid(column = 3, row = 5)
        
        
    def start_calculation(self):
        bp = int(self.var_bp.get())
        times = int(self.var_times.get())
        f = Fuzion()

        for i in range(0, 60):
            successes = 0
            fails = 0
            #print(i)
            for a in range(0, times):
                s_throw = bp + f.Roll()
                if s_throw >= i:
                    successes += 1
                else:
                    fails += 1

                divider = successes + fails
                percent = successes / divider
                percent = percent * 100
                text = '%.5f' % percent
                self.vars[i].set(text)
                self.root.update()
                
                
                
                

