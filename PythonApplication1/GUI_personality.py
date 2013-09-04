from tkinter import *
from tkinter import ttk
from random import choice
from GUI_sub_per import GUI_per_sub
class GUI_personality(object):
    """description of class"""
    def Assign(self, master, controller):
        self.contr = controller
        self.personality_frame = ttk.Labelframe(master, text='Personality')
        
        self.stringvars={}
        self.d_stringvars={}

        p = ttk.Panedwindow(self.personality_frame, orient=HORIZONTAL)
        p2 = ttk.Panedwindow(self.personality_frame, orient=HORIZONTAL)

        f1 = ttk.Labelframe(p, text='Basic Info', width=100, height=100)
        f2 = ttk.Labelframe(p, text='Psychological profile', width=100, height=100)
        f3 = ttk.Labelframe(p2, text='Dress & Personal style', width=100, height=100)
        
        p.add(f1)
        p.add(f2)

        p2.add(f3)

        lbl_p_name = ttk.Label(f1, text='Player name')
        lbl_c_fname = ttk.Label(f1, text='First name')
        lbl_c_sname = ttk.Label(f1, text='Second name')
        lbl_c_lname = ttk.Label(f1, text='Last name')
        lbl_n_name = ttk.Label(f1, text='Nick name')
        lbl_age = ttk.Label(f1, text='Age')

        var_p_name = StringVar()
        self.var_c_fname = StringVar()
        self.var_c_sname = StringVar()
        self.var_c_lname = StringVar()
        self.var_c_n_name = StringVar()
        var_age = StringVar()

        entry_p_name = ttk.Entry(f1, textvariable=var_p_name)
        entry_c_fname = ttk.Entry(f1, textvariable=self.var_c_fname)
        entry_c_sname = ttk.Entry(f1, textvariable=self.var_c_sname)
        entry_c_lname = ttk.Entry(f1, textvariable=self.var_c_lname)
        entry_c_n_name = ttk.Entry(f1, textvariable=self.var_c_n_name)
        entry_age = ttk.Entry(f1, textvariable=var_age)

        button_r_fname = ttk.Button(f1, text = 'Random', command = self.random_f_name)
        button_r_sname = ttk.Button(f1, text = 'Random', command = self.random_s_name)
        button_r_lname = ttk.Button(f1, text = 'Random', command = self.random_l_name)
        button_r_n_name = ttk.Button(f1, text = 'Random', command = self.random_n_name)

        gender_frame = ttk.Labelframe(f1, text="Gender")
        self.var_gender = StringVar()

        radio_male = ttk.Radiobutton(gender_frame, text='Male', variable=self.var_gender, value="Male")
        radio_female = ttk.Radiobutton(gender_frame, text='Female', variable=self.var_gender, value="Female")

        #PSYCHOLOGICAL PROFILE
        #PRIME MOTIVATION
        prime = GUI_per_sub(f2, 'source/prime_motivation.txt',      'Prime Motivation: ')
        prime_frame=prime.frame
        prime_frame.grid(column = 0, row = 0, sticky=(W))

        #Most valued person & posession
        valued_person = GUI_per_sub(f2,'source/valued_person.txt',  'Most valued person: ')
        valued_person_frame = valued_person.frame
        valued_person_frame.grid(column =  0, row = 1, sticky=(W))

        valued_pos = GUI_per_sub(f2, 'source/valued_posession.txt', 'Most valued posession: ')
        valued_pos_frame = valued_pos.frame
        valued_pos_frame.grid(column = 0, row = 2, sticky=(W))

        valued_people = GUI_per_sub(f2, 'source/valued_people.txt', 'How do you feel about most people: ')
        valued_people_frame = valued_people.frame
        valued_people_frame.grid(column = 0, row = 3, sticky=(W))

        #INMODE
        inmode = GUI_per_sub(f2, 'source/inmode.txt', 'Inmode:')
        inmode_frame = inmode.frame
        inmode_frame.grid(column = 0, row = 4, sticky=(W))

        #EXMODE
        exmode = GUI_per_sub(f2, 'source/exmode.txt', 'Exmode:')
        exmode_frame = exmode.frame
        exmode_frame.grid(column = 0, row = 5, sticky=(W))

        f4 = ttk.Frame(f2)
        #QUIRKS
       
        quirks = multi_value(f4, 'source/quirks.txt', 'Quirks')
        quirks_frame = quirks.frame
        quirks_frame.grid(column = 0, row = 0, sticky=(W))


        #DISORDERS
        disorders = multi_value(f4, 'source/disorders.txt', 'Disorders')
        disorder_frame = disorders.frame
        disorder_frame.grid(column = 1, row = 0, sticky=(W))

        #PHOBIAS
        phobias = multi_value(f4, 'source/phobias.txt', 'Phobias', leveys = 30, rivit=25)
        phobias_frame = phobias.frame
        phobias_frame.grid(column = 2, row = 0, sticky = (W))

        #DRESS & PERSONAL STYLE
        clothes = multi_value(f3, 'source/clothes.txt','Clothes')
        clothes_frame = clothes.frame
        clothes_frame.grid(column = 0, row = 0)

        hair = multi_value(f3, 'source/hair.txt', 'Hair')
        hair_frame = hair.frame
        hair_frame.grid(column = 1, row = 0)

        affe = multi_value(f3, 'source/affections.txt', 'Affections')
        affe_frame = affe.frame
        affe_frame.grid(column = 2, row = 0)



        p.grid(column = 0, row = 0, sticky=(N))
        p2.grid(column = 0, row = 1, sticky=(W))
        f1.grid(column = 0, row = 0, sticky=(N))
        f2.grid(column = 1, row = 0)
        f3.grid(column = 0, row = 6)
        f4.grid(column = 0, row = 6, sticky=(W))
        lbl_p_name.grid(column = 0, row = 0, sticky=(W))
        lbl_c_fname.grid(column = 0, row = 1, sticky=(W))
        lbl_c_sname.grid(column = 0, row = 2, sticky=(W))
        lbl_c_lname.grid(column = 0, row = 3, sticky=(W))
        lbl_n_name.grid(column = 0, row = 4, sticky=(W))
        lbl_age.grid(column = 0, row = 5, sticky=(W))

        entry_p_name.grid(column = 1, row = 0)
        entry_c_fname.grid(column = 1, row = 1)
        entry_c_sname.grid(column = 1, row = 2)
        entry_c_lname.grid(column = 1, row = 3)
        entry_c_n_name.grid(column = 1, row = 4)
        entry_age.grid(column = 1, row = 5)

        button_r_fname.grid(column = 2, row = 1)
        button_r_sname.grid(column = 2, row = 2)
        button_r_lname.grid(column = 2, row = 3)
        button_r_n_name.grid(column = 2, row = 4)

        gender_frame.grid(column = 0, row = 6)
        radio_male.grid(column = 0, row = 0)
        radio_female.grid(column = 1, row = 0)

        

        

        return self.personality_frame

    def random_f_name(self):
        name = self.contr.get_r_name("first", self.var_gender.get())
        self.var_c_fname.set(name)
    def random_s_name(self):
        name = self.contr.get_r_name("second", self.var_gender.get())
        self.var_c_sname.set(name)
    def random_l_name(self):
        name = self.contr.get_r_name("last", self.var_gender.get())
        self.var_c_lname.set(name)
    def random_n_name(self):
        name = self.contr.get_r_name("nick", self.var_gender.get())
        self.var_c_n_name.set(name)

    def Read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

class multi_value:
    def __init__(self, master, filepath, label_text='default', korkeus=5, leveys = 15, rivit = 10):
        self.valuelist = []
        self.stringvars = {}
        self.lines = rivit
        self.Read_file(filepath, self.valuelist)
        self.topic=label_text
        self.frame = ttk.Labelframe(master, text=label_text)

        self.listbox = Listbox(self.frame, height = korkeus,  width = leveys)
        self.button_choose = ttk.Button(self.frame, text='Choose..', command = self.choose_values)
        self.button_random = ttk.Button(self.frame, text='Random', command = self.random_value)

        self.frame.grid(column = 0, row = 0)
        self.listbox.grid(column = 0, row = 0)
        self.button_choose.grid(column = 0, row = 1)
        self.button_random.grid(column = 0, row= 2)

    def Read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

    def choose_values(self):
        self.window = Toplevel(self.frame)
        value_frame = ttk.Labelframe(self.window, text=self.topic)
        radio_elements = {} 
        self.stringvars = {}

        for value in self.valuelist:
            s = StringVar()
            s.set("off")
            self.stringvars[value] = s
            radio_elements[value] = ttk.Checkbutton(value_frame, text=value, variable=self.stringvars[value], onvalue=value, offvalue="off", command=self.set_value)

        i=0
        c=0
        for item, value in radio_elements.items():
            value.grid(column = c, row = i, sticky=(W))
            i = i+1
            if i==self.lines:
                i=0;
                c= c+1
            
        value_frame.grid(column = 0, row = 0)
        ok = ttk.Button(value_frame, text='Close', command=self.close_value)
        ok.grid(column = 0, row = self.lines+1, sticky = (W))

    def random_value(self):
        x = choice(self.valuelist)
        self.stringvars[x]=x
        self.set_value()

    def set_value(self):
        self.listbox.delete(0, END)
        for key, value in self.stringvars.items():
            try:
                if value.get() != "off":
                    
                    self.listbox.insert(END, value.get())
            except Exception:
                if value != "off":
                    self.listbox.insert(END, value)

    def close_value(self):
        self.window.destroy()
