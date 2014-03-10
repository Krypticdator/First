from tkinter import *
from tkinter import ttk
from Controller import Controller
class GUI_header(object):
    """description of class"""
    def __init__(self, master, contr=Controller()):
        self.contr = contr
        self.frame = ttk.Frame(master)
        self.contr.datasets['headers'].append(self)

        self.max_cpoints=60
        self.max_opoints=50

        #c_max_text = '/' + str(self.max_cpoints)
        

        self.lbl_cpoints = ttk.Label(self.frame, text='CP')
        #self.lbl_cpoints_max=ttk.Label(self.frame, text=c_max_text)
        self.lbl_opoints = ttk.Label(self.frame, text='OP')
        self.lbl_money = ttk.Label(self.frame, text ='DCD')
        self.lbl_hum = ttk.Label(self.frame, text='Hum')

        self.var_cpoints = StringVar()
        self.var_opoints = StringVar()
        self.var_money = StringVar()
        self.var_hum = StringVar()

        self.lbl_var_cpoints = ttk.Label(self.frame, textvariable=self.var_cpoints)
        self.lbl_var_opoints = ttk.Label(self.frame, textvariable=self.var_opoints)
        self.lbl_var_money = ttk.Label(self.frame, textvariable=self.var_money)
        self.lbl_var_hum = ttk.Label(self.frame, textvariable=self.var_hum)

        self.frame.grid(column=0, row=0, sticky=(W))
        self.lbl_cpoints.grid(column=0, row=0, sticky=(W))
        self.lbl_var_cpoints.grid(column=1, row=0, sticky=(W))
        self.lbl_opoints.grid(column=2, row=0, sticky=(W))
        self.lbl_var_opoints.grid(column=3,row=0, sticky=(W))
        self.lbl_money.grid(column=4, row=0, sticky=(W))
        self.lbl_var_money.grid(column=5, row=0, sticky=(W))
        #self.lbl_cpoints_max.grid(column=2, row=0)

        #self.recalculate()

    def recalculate(self):
        '''statbox = self.contr.datasets['stats']
        skills = self.contr.get_ability_dictionary('skills')
        perks = self.contr.get_ability_dictionary('perks')
        cpoint_sum = 0
        opoint_sum = 0

        for key, value in statbox.variables.items():
            cpoint_sum = cpoint_sum + int(value.get())

        for key, value in skills.items():
            if int(value)!=0:
                opoint_sum = opoint_sum + int(value)

        for key, value in perks.items():
            if key.count('Favor'):
                cost = int(value) * 0.5
                opoint_sum = opoint_sum + cost
            elif key.count('Wealth'):
                cost = int(value) * 5
                opoint_sum = opoint_sum + cost
            else:
                opoint_sum = opoint_sum + int(value)


        cpoint_sum = self.max_cpoints - cpoint_sum
        opoint_sum = self.max_opoints - opoint_sum

        cpoint_text = str(cpoint_sum) + '/' + str(self.max_cpoints)
        opoint_text = str(opoint_sum) + '/' + str(self.max_opoints)

        self.var_cpoints.set(str(cpoint_text))
        self.var_opoints.set(opoint_text)'''





