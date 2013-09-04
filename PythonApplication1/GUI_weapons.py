from tkinter import *
from tkinter import ttk
from GUI_wpn_info import GUI_wpn_info
from GUI_factory import Category_UI

class GUI_weapons(Category_UI):
    """description of class"""
    
    def __init__(self, master, controller):
        super().__init__(master, controller, frametext='Weapons', first_header='Categories', second_header='Available', third_header='Description')
        self.wpn_info = GUI_wpn_info()
        self.wpn_info_frame = self.wpn_info.Assign(self.p, controller)
        self.f3.destroy()
        self.populate_box(self.box_categories, self.contr.settings.wpn_classes)
        self.p.add(self.wpn_info_frame)

        self.ava_l_pistols = []
        self.ava_m_pistols = []
        self.ava_h_pistols = []
        self.ava_v_h_pistols = []
        self.ava_l_submachineguns = []
        self.ava_m_submachineguns = []
        self.ava_h_submachineguns = []
        self.ava_shotguns = []
        self.ava_a_rifles = []
        self.ava_s_rifles = []
        self.ava_o_rifles = []
        self.ava_machineguns = []

        self.define_wpn_available(self.contr.settings.light_pistols, self.ava_l_pistols)
        self.define_wpn_available(self.contr.settings.medium_pistols, self.ava_m_pistols)
        self.define_wpn_available(self.contr.settings.heavy_pistols, self.ava_h_pistols)
        self.define_wpn_available(self.contr.settings.v_heavy_pistols, self.ava_v_h_pistols)
        self.define_wpn_available(self.contr.settings.l_submachineguns, self.ava_l_submachineguns)
        self.define_wpn_available(self.contr.settings.m_submachineguns, self.ava_m_submachineguns)
        self.define_wpn_available(self.contr.settings.h_submachineguns, self.ava_h_submachineguns)
        self.define_wpn_available(self.contr.settings.shotguns, self.ava_shotguns)
        self.define_wpn_available(self.contr.settings.a_rifles, self.ava_a_rifles)
        self.define_wpn_available(self.contr.settings.s_rifles, self.ava_s_rifles)
        self.define_wpn_available(self.contr.settings.o_rifles, self.ava_o_rifles)
        self.define_wpn_available(self.contr.settings.machineguns, self.ava_machineguns)

        self.add_category_items("Light Pistols", self.ava_l_pistols)
        self.add_category_items("Medium Pistols", self.ava_m_pistols)
        self.add_category_items('Heavy Pistols', self.ava_h_pistols)
        self.add_category_items('Very Heavy Pistols', self.ava_v_h_pistols)
        self.add_category_items('Light Submachineguns', self.ava_l_submachineguns)
        self.add_category_items('Medium Submachineguns', self.ava_m_submachineguns)
        self.add_category_items('Heavy Submachineguns', self.ava_h_submachineguns)
        self.add_category_items('Shotguns', self.ava_shotguns)
        self.add_category_items('Assault Rifles', self.ava_a_rifles)
        self.add_category_items('Sniper Rifles', self.ava_s_rifles)
        self.add_category_items('Other Rifles', self.ava_o_rifles)
        self.add_category_items('Machineguns', self.ava_machineguns)
       
        self.add_category_items('Failed', self.contr.settings.failed_wpns)

        self.box_list.bind('<<ListboxSelect>>', self.show_wpn_details)
    
    def define_wpn_available(self, wpn_list, target_list):

        for wpn in wpn_list:
            roll = self.contr.get_Wpn_availability()
            diff = wpn.getAttribute("Avail_diff")
            #print("roll: ", roll, "diff: ", diff)
            if roll >= diff:
                #print("INCLUDED")
                wpn_name = wpn.getAttribute("Name")
                target_list.append(wpn_name)    

    def show_wpn_details(self, *args):
        self.wpn_info.show_wpn_details(self.box_list)

    def populate_box(self, box, list, filepath='none'):
        if filepath == 'none':
            #list.sort()
            for item in list:
                box.insert(END, item)
            box.selection_set(0)
        else:
            self.contr.settings.Read_file(filepath, list)
            #list.sort()
            for item in list:
                box.insert(END, item)
            box.selection_set(0)
   