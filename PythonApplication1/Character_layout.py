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

class Character_Layout():
    """description of class"""
    def __init__(self):
        self.contr = Controller()
        root = Tk()
        content = ttk.Frame(root)
        self.n = ttk.Notebook(content)
        
        self.stats_box = GUI_stats_box()
        #wpn_box = GUI_weapons()
        #skill = GUI_skills()
        #comp = GUI_complications()
        #talents = GUI_talents()
        #perks = GUI_perks()
        self.personality = GUI_personality()
        self.wpns = GUI_weapons(self.n, self.contr)
        self.perks = GUI_perks(self.n, self.contr)
        self.skills = GUI_skills(self.n, self.contr)
        self.comp = GUI_complications(self.n, self.contr)
        self.talents = GUI_talents(self.n, self.contr)
        
        #skillframe = skill.Assign(n, contr)
        self.skillframe = self.skills.frame
        self.stats_frame = self.stats_box.Assign(self.n, self.contr)
        #wpn_frame = wpn_box.Assign(n, contr)
        self.wpn_frame = self.wpns.frame
        #comp_frame = comp.Assign(n, contr)
        self.comp_frame = self.comp.frame
        #talent_frame = talents.Assign(n, contr)
        self.talent_frame = self.talents.frame
        #perk_frame = perks.Assign(n, contr)
        self.perk_frame = self.perks.frame
        self.personality_frame = self.personality.Assign(self.n, self.contr)
        self.lifepath_frame = GUI_Lifepath(self.n, self.contr)

        self.n.add(self.stats_frame, text='Stats')
        self.n.add(self.wpn_frame, text='Weapons')
        self.n.add(self.skillframe, text = 'Skills')
        self.n.add(self.comp_frame, text = 'Complications')
        self.n.add(self.talent_frame, text = 'Talents')
        self.n.add(self.perk_frame, text = 'Perks')
        self.n.add(self.personality_frame, text = 'Personality')
        self.n.add(self.lifepath_frame.frame, text = 'Lifepath')
        
      
        content.grid(column=0, row=0)
        self.n.grid(column=0, row=0)
        
        root.mainloop()