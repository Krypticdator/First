from tkinter import *
from tkinter import ttk
from GUI_d_stats import GUI_d_stats
from GUI_stat_info import GUI_stat_info

class GUI_stats_box(object):
    """description of class"""  
        
    def Assign(self, master, controller):
        self.contr = controller

        self.stats_frame = ttk.Labelframe(master, text='Stats')
        
        self.d_stat = GUI_d_stats()
        self.d_stat_frame = self.d_stat.Assign(self.stats_frame, controller)
        self.stat_info = GUI_stat_info()
        self.stat_info_frame = self.stat_info.Assign(self.stats_frame, controller)
        self.stat_box = Stat_box(self.stats_frame, controller, self.stat_info, self.d_stat)
        
        stat_box_frame = self.stat_box.frame
        stat_box_frame.grid(column = 0, row = 0)
        self.stat_info_frame.grid(column = 1, row = 0, rowspan=11, sticky=(N))

        self.d_stat_frame.grid(column = 4, row = 0, rowspan=11, sticky=(W, N))

        return self.stats_frame


class Stat_box:
    def __init__(self, master, controller, info_box, derived_stats):
        self.frame = ttk.Labelframe(master, text="Stats")
        self.contr = controller
        self.stats = []
        self.labels = {}
        self.r_labels = {}
        self.variables = {}
        self.r_variables= {}
        self.spinners = {}
        self.descr_text = ''
        self.info_box = info_box
        self.derived_stats = derived_stats
        

        self.contr.settings.Read_file('source/attributes.txt', self.stats)

        for stat in self.stats:
            self.labels[stat] = ttk.Label(self.frame, text=stat)
            self.variables[stat] = StringVar()
            self.r_variables[stat] = StringVar()
            self.spinners[stat] = Spinbox(self.frame, from_=1.0, to=10, textvariable = self.variables[stat], width = 2, command=self.rating_labels)
            self.r_labels[stat] = ttk.Label(self.frame, textvariable = self.r_variables[stat])

        self.rating_labels()
        rownum = 0
        columnnum = 0

        self.frame.grid(column=columnnum, row = rownum)

        for stat in self.stats:
                for key, value in self.labels.items():
                    if stat == key:
                        value.grid(column=columnnum,row=rownum)
                        rownum = rownum +1
        rownum = 0
        columnnum = 1
        for stat in self.stats:
                for key, value in self.spinners.items():
                    if stat == key:
                        value.grid(column=columnnum,row=rownum)
                        rownum = rownum +1
        rownum = 0
        columnnum = 2    
        for stat in self.stats:
                for key, value in self.r_labels.items():
                    if stat == key:
                        value.grid(column=columnnum,row=rownum)
                        rownum = rownum +1

    def rating_labels(self):
        for stat in self.stats:
            self.r_variables[stat].set(self.Attribute_rating(self.spinners[stat].get()))

        local = {}
        for stat in self.stats:
            local[stat] = self.spinners[stat].get()

        char = {}
        for stat in self.stats:
            char[stat] = self.contr.getChar_stat(stat)
       
        for stat, number in local.items():
            if int(local[stat]) != int(char[stat]):
               self.descr_text = stat
               self.contr.setChar_stat(stat, self.variables[stat].get()) 
               self.info_box.setText(self.contr.settings.attribute_descriptions[self.descr_text])
               self.derived_stats.update_stats()

    def Attribute_rating(self, num):
        descr = ""
        num = int(num)
        if num == 1:
            descr = "Challenged"
        if num == 2:
            descr = "Everyday"
        if num == 3 or num == 4:
            descr = "Competent"
        if num == 5 or num == 6:
            descr = "Heroic"
        if num == 7 or num == 8:
            descr = "Incredible"
        if num == 9 or num == 10:
            descr = "Legendary"

        return descr
