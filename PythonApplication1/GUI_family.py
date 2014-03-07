from tkinter import *
from tkinter import ttk
from GUI_sub_per import GUI_per_sub
from Lifepath import Family
from dice import Dice
from Filecontrol import Filecontrol
from random import choice

class GUI_family(Filecontrol):
    """description of class"""
    def __init__(self, master, controller):
        self.contr = controller
        self.frame = ttk.Labelframe(master, text='Family')
        f = Family()
        var_width_num=100
        self.family_rank = GUI_per_sub(self.frame, "lifepath/family/family_rank.txt", "Family rank", var_width=var_width_num, controller=self.contr)
        self.parent_who = GUI_per_sub(self.frame, 'lifepath/family/family_is.txt', 'Your parents were', var_width=var_width_num, controller=self.contr)
        self.parent_status = GUI_per_sub(self.frame, 'lifepath/family/family_is_2.txt', 'Parent status', var_width=var_width_num, controller=self.contr)
        self.parent_event = GUI_per_sub(self.frame, 'lifepath/family/family_something_happened.txt', 'Parent event', var_width=var_width_num, controller=self.contr)
        self.parent_event.var.set('nothing bad happened to parents')
        self.family_status = GUI_per_sub(self.frame, 'lifepath/family/family_status.txt','Family status', var_width=var_width_num, controller=self.contr)
        self.family_tragedy = GUI_per_sub(self.frame, 'lifepath/family/family_tragedy.txt', 'Family event', var_width=var_width_num, controller=self.contr)
        self.family_tragedy.var.set('nothing bad happened to family')
        self.childhood_envi = GUI_per_sub(self.frame, 'lifepath/family/childhood_enviroment.txt', 'Childhood enviroment', var_width=var_width_num, controller=self.contr)
        self.childhood_trauma = GUI_per_sub(self.frame, 'lifepath/family/childhood_trauma.txt', 'Childhood trauma/fortune', var_width=var_width_num, controller=self.contr)
        self.family_contact = GUI_per_sub(self.frame, 'lifepath/family/family_contact.txt', 'Family contact', var_width=var_width_num, controller=self.contr)
        self.btn_siblings = ttk.Button(self.frame, text='Generate siblings', command=self.gen_siblings)
        self.btn_show_siblings = ttk.Button(self.frame, text='Show siblings', command=self.show_siblings)
        self.sibling_var = StringVar()
        self.lbl_siblings = ttk.Label(self.frame, textvariable=self.sibling_var)

        self.family_rank.frame.grid(column=0, row=0)
        self.parent_who.frame.grid(column=0, row=1)
        self.parent_status.frame.grid(column=0, row=2)
        self.parent_event.frame.grid(column=0, row=3)
        self.family_status.frame.grid(column=0, row=4)
        self.family_tragedy.frame.grid(column=0, row=5)
        self.childhood_envi.frame.grid(column=0, row=6)
        self.childhood_trauma.frame.grid(column=0, row=7)
        self.family_contact.frame.grid(column=0, row=8)
        self.btn_siblings.grid(column=0, row=9, sticky=(W))
        self.lbl_siblings.grid(column=0, row=10, sticky=(W))
        self.btn_show_siblings.grid(column=0, row=11, sticky=(W))

        

    def gen_siblings(self):
        d = Dice()
        roll = d.Roll(1, 10)
        self.relations = []
        self.siblings = []
        self.gender_table = []
        self.gender_table.append('Male')
        self.gender_table.append('Female')
        self.read_file('lifepath/family/family_siblings.txt', self.relations)
        little_num = 1
        big_num= 1
        if roll>0 and roll<8:
            for i in range(0, roll):
                gender = choice(self.gender_table)
                first=self.contr.get_r_name('first', gender)
                second=self.contr.get_r_name('second', gender)
                last=self.contr.datasets['last name']
                nick = self.contr.get_r_name('nick', gender)
                name = first + ' ' + second + ' ' + nick + ' ' + last.get()
                age=int(self.contr.datasets['age'].get())
                relative_age = d.Roll(1,2)
                if relative_age ==1:
                    age= age-little_num
                    little_num = little_num +1
                else:
                    age= age + big_num
                    big_num = big_num +1

                relation = choice(self.relations)
                member = family_member(name, relation, gender, age)
                self.siblings.append(member)
            self.sibling_var.set('you have ' +str(roll) + ' siblings')
            self.contr.datasets['siblings'] = self.siblings
        else:
            self.sibling_var.set('you are the only child')
            member = family_member('you are the only child','none','none',0)
            self.siblings.append(member)
            self.contr.datasets['siblings'] = self.siblings

    def show_siblings(self):
        self.window = Toplevel(self.frame)
        frame = ttk.Labelframe(self.window, text='siblings list')
        nameframe = ttk.Labelframe(frame, text='name')
        ageframe = ttk.Labelframe(frame, text='age')
        genderframe = ttk.Labelframe(frame, text='gender')
        relationframe = ttk.Labelframe(frame, text='relation')

        column_num=0
        row_num = 0
        for member in self.siblings:
            label = ttk.Label(nameframe, text=member.name)
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        column_num=0
        row_num = 0
        for member in self.siblings:
            label = ttk.Label(genderframe, text=member.gender)
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        column_num=0
        row_num = 0
        for member in self.siblings:
            label = ttk.Label(ageframe, text=member.age)
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        column_num=0
        row_num = 0
        for member in self.siblings:
            label = ttk.Label(relationframe, text=member.relation)
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        frame.grid(column=0, row=0)
        nameframe.grid(column=1, row=0)
        genderframe.grid(column=2, row=0)
        ageframe.grid(column=3, row=0)
        relationframe.grid(column=4, row=0)
        
class family_member:
    def __init__(self, name='undefined', relation='undefined', gender='undecided', age=0):
        self.name=name
        self.relation=relation
        self.gender=gender
        self.age=age
        





