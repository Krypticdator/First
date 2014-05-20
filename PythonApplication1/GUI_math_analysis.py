from tkinter import *
from tkinter import ttk
from Fuzion import Fuzion
#from decimal import *
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
        button = ttk.Button(self.frame, text='Start', command=self.grand_loop)

        self.var_state = StringVar()
        self.lbl_bottom = ttk.Label(self.frame, textvariable=self.var_state)
        
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
        self.lbl_bottom.grid(column=4, row = 5)
        #self.p.grid(column = 3, row = 5)
        
    def grand_loop(self):
        for i in range(0,60):
            self.start_calculation(i)  
    def start_calculation(self, bp=0):
        #bp = int(self.var_bp.get())
        
        #times = int(self.var_times.get())
        times = 2000000000
        f = Fuzion()
        
        for i in range(0, 60):
            successes = 0
            fails = 0
            checkpoint = 0
            checkpoint_result = 0
            #print(i)
            for a in range(0, times):
                s_throw = bp + f.Roll()
                if s_throw >= i:
                    successes += 1
                    checkpoint +=1
                else:
                    fails += 1
                    checkpoint +=1

                divider = successes + fails
                percent = successes / divider
                percent = percent * 100

                if checkpoint ==10000:
                    checkpoint=0
                    if abs(percent - checkpoint_result) < 0.01:
                        #print('final calculations: ' + str(divider))
                        break
                    else:
                        checkpoint_result=percent

                

                text = '%.5f' % percent
                self.vars[i].set(text)
                self.var_state.set(str(bp))
                self.root.update()
            file = open('math_results.txt', 'a')
            file.write(str(bp) + ';' +str(i) +';' +str(self.vars[i].get()) + '\n')
            file.close()

class CombatDamage(object):
    def __init__(self, master, root):
        self.root = root
        self.frame = ttk.Frame(master)
        self.lbl_bp = ttk.Label(self.frame, text='bp')
        self.lbl_dmg = ttk.Label(self.frame, text='dmg')
        self.lbl_ac = ttk.Label(self.frame, text='ac')
        self.lbl_e_bp = ttk.Label(self.frame, text='enemy bp')
        self.lbl_dmg_change = ttk.Label(self.frame, text='change of damage')
        self.lbl_dmg_per_turn = ttk.Label(self.frame, text='dmg per turn')
        self.lbl_average_dmg = ttk.Label(self.frame, text='average dmg')
        self.lbl_lowest_dmg = ttk.Label(self.frame, text='lowest dmg')
        self.lbl_highest_dmg = ttk.Label(self.frame, text='highest dmg')

        self.var_bp = StringVar()
        self.var_dmg = StringVar()
        self.var_ac = StringVar()
        self.var_e_bp = StringVar()
        self.var_dmg_change = StringVar()
        self.var_dmg_per_turn = StringVar()
        self.var_average_dmg = StringVar()
        self.var_lowest_dmg = StringVar()
        self.var_highest_dmg = StringVar()

        self.lbl_val_bp = ttk.Label(self.frame, textvariable=self.var_bp)
        self.lbl_val_dmg = ttk.Label(self.frame, textvariable=self.var_dmg)
        self.lbl_val_ac = ttk.Label(self.frame, textvariable=self.var_ac)
        self.lbl_val_e_bp = ttk.Label(self.frame, textvariable=self.var_e_bp)
        self.lbl_val_dmg_change = ttk.Label(self.frame, textvariable=self.var_dmg_change)
        self.lbl_val_dmg_per_turn = ttk.Label(self.frame, textvariable=self.var_dmg_per_turn)
        self.lbl_val_lowest_dmg = ttk.Label(self.frame, textvariable=self.var_lowest_dmg)
        self.lbl_val_highest_dmg = ttk.Label(self.frame, textvariable=self.var_highest_dmg)

        self.btn_start = ttk.Button(self.frame, text='start')

        self.lbl_bp.grid(column=0, row=0)
        self.lbl_val_bp.grid(column=1, row=0)
        self.lbl_dmg.grid(column=0,row=1)
        self.lbl_val_dmg(column=1, row=1)
        self.lbl_e_bp.grid(column=2, row=0)
        self.lbl_ac.grid(column=3, row=0) 


        


        
                
                
                
                

