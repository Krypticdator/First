from tkinter import *
from tkinter import ttk
from Filecontrol import Filecontrol
from GUI_factory import text_and_inputfield
from xml_file import xml_file
import xml.etree.ElementTree as ET
class GUI_item_creator(Filecontrol):
    """description of class"""
    def __init__(self, master):
        super().__init__()
        self.read_file_to_segments('source/armor/hitlocations.txt', ';')
        self.frame = ttk.Frame(master)
        self.sp_frame = ttk.Labelframe(self.frame, text='SP')
        self.info_frame = ttk.Labelframe(self.frame, text='Basic info')
        self.elements = {}

        master.title('armor creation')
        master.option_add('*tearOff', FALSE)
        menubar = Menu(master)
        master['menu'] = menubar
        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.new)
        menu_file.add_command(label='Save', command = self.save)

        self.r_elements = {}
        req_fields = []
        req_fields.append('brand')
        req_fields.append('name')
        req_fields.append('ev')
        req_fields.append('cost')
        req_fields.append('description')
        req_fields.append('type')

        for field in req_fields:
            self.r_elements[field] = text_and_inputfield(self.info_frame, field, StringVar(), width_num=20)
        
        print(self.segmented_file_array)
        self.segmented_file_array.pop(7)
        for hitlocation in self.segmented_file_array:
            variable = StringVar()
            self.elements[hitlocation[1]] = text_and_inputfield(self.sp_frame, hitlocation[1], variable)
        print(self.elements)
        
        self.frame.grid(column = 0, row = 0)
        self.sp_frame.grid(column= 1, row = 0)
        self.info_frame.grid(column = 0, row = 0, sticky=(N))
        
        row_num =0
        for item in req_fields:
            for key, element in self.r_elements.items():
                if item==key:
                    element.frame.grid(column = 0, row = row_num, sticky=(N))
                    row_num = row_num +1

        row_num =0
        for item in self.segmented_file_array:
            for key, element in self.elements.items():
                if item[1]==key:
                    element.frame.grid(column = 0, row = row_num)
                    row_num = row_num +1
    def new(self):
        for key, value in self.r_elements.items():
            value.entry.delete(0, END)
        for key, value in self.elements.items():
            value.entry.delete(0, END)
    def save(self):
        file = xml_file()
        print('saving')
        tree = file.load_file('data/armors.xml')
        if tree == 'error':
            print('error if lause')
            file.create_root("armors")
            file.create_sub_element('armor','root')
            for key, item in self.r_elements.items():
                file.create_sub_element(key, 'armor')
                file.set_text(item.variable.get(), key)

            file.create_sub_element('sp', 'armor')
            for key, item in self.elements.items():
                file.create_sub_element(key, 'sp')
                file.set_text(item.variable.get(), key)

            file.save_file('data/armors.xml')
        else:
            file.load_file('data/armors.xml')
            file.create_sub_element('armor', 'root')
            for key, item in self.r_elements.items():
                file.create_sub_element(key, 'armor')
                file.set_text(item.variable.get(), key)

            file.create_sub_element('sp', 'armor')
            for key, item in self.elements.items():
                file.create_sub_element(key, 'sp')
                file.set_text(item.variable.get(), key)
            file.save_file('data/armors.xml')
            

            

