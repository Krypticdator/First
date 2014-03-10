from tkinter import *
from tkinter import ttk
from Controller import Controller
from GUI_stats_box import GUI_stats_box
from GUI_weapons import GUI_weapons
from GUI_stat_info import GUI_stat_info
from GUI_skills import GUI_skills
from GUI_complications import GUI_complications
from GUI_talents import GUI_talents
from GUI_perks import GUI_perks
from GUI_personality import GUI_personality
from GUI_Lifepath import GUI_Lifepath
from GUI_armor import GUI_armor
from GUI_cyber import GUI_cyber
from cp20ex import cp20ex
from GUI_items_menu import GUI_items_menu
from GUI_family import GUI_family
from GUI_header import GUI_header

class Character_Layout():
    """description of class"""
    def __init__(self, master):
        self.contr = Controller()
        content = ttk.Frame(master)
        self.n = ttk.Notebook(content)

        master.option_add('*tearOff', FALSE)
        menubar = Menu(master)
        master['menu'] = menubar
        menu_file = Menu(menubar)
        menu_generate = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menubar.add_cascade(menu=menu_generate, label='Generate')
        menu_file.add_command(label='Save', command = self.save)
        menu_generate.add_command(label = 'Lifepath', command=self.gen_lifepath)
        menu_generate.add_command(label = 'Weapons', command=self.gen_wpns)
        
        self.stats_box = GUI_stats_box()
        #wpn_box = GUI_weapons()
        #skill = GUI_skills()
        #comp = GUI_complications()
        #talents = GUI_talents()
        #perks = GUI_perks()
        self.personality = GUI_personality()
        self.wpns = GUI_weapons(self.n, self.contr)
        self.armor = GUI_armor(self.n, self.contr)
        self.perks = GUI_perks(self.n, self.contr)
        self.skills = GUI_skills(self.n, self.contr)
        self.comp = GUI_complications(self.n, self.contr)
        self.talents = GUI_talents(self.n, self.contr)
        self.cyber = GUI_cyber(self.n, self.contr)
        self.items = GUI_items_menu(self.n, self.contr)
        self.family = GUI_family(self.n, self.contr)
        
        #skillframe = skill.Assign(n, contr)
        self.skillframe = self.skills.frame
        self.stats_frame = self.stats_box.Assign(self.n, self.contr)
        #wpn_frame = wpn_box.Assign(n, contr)
        self.wpn_frame = self.wpns.frame
        self.armor_frame = self.armor.frame
        #comp_frame = comp.Assign(n, contr)
        self.comp_frame = self.comp.frame
        #talent_frame = talents.Assign(n, contr)
        self.talent_frame = self.talents.frame
        #perk_frame = perks.Assign(n, contr)
        self.perk_frame = self.perks.frame
        self.personality_frame = self.personality.Assign(self.n, self.contr)
        self.lifepath_frame = GUI_Lifepath(self.n, self.contr)
        self.cyber_frame = self.cyber.frame
        self.item_frame = self.items.frame
        self.family_frame = self.family.frame

        self.n.add(self.personality_frame, text = 'Personality')
        self.n.add(self.family_frame, text = 'Family')
        self.n.add(self.lifepath_frame.frame, text = 'Lifepath')
        self.n.add(self.stats_frame, text='Stats')
        self.n.add(self.skillframe, text = 'Skills')
        self.n.add(self.comp_frame, text = 'Complications')
        self.n.add(self.talent_frame, text = 'Talents')
        self.n.add(self.perk_frame, text = 'Perks')
        self.n.add(self.item_frame, text='Items')
        self.n.add(self.wpn_frame, text='Weapons')
        self.n.add(self.armor_frame, text='Armors')
        self.n.add(self.cyber_frame, text="Cybernetics")
        
        
        
        
        
        
        
        
      
        content.grid(column=0, row=0)
        self.n.grid(column=0, row=0)

        cp = cp20ex()
    def save(self):
        self.contr.save()
        self.contr.settings.make_preference_xml()

    def gen_lifepath(self):
        self.lifepath_frame.init_years()

    def gen_wpns(self):
        self.wpns.init_wpns_list()
        
      