from tkinter import *
from tkinter import ttk
class GUI_items(object):
    """editor for making items"""
    def Assign(self, master, controller):
        self.contr = controller
        self.items_frame = ttk.Labelframe(master, text='Items')

        var_attribute = StringVar()
        var_attribute_value = StringVar()
        var_action = StringVar()
        var_definitions = StringVar()
        var_needed_items = StringVar()
        var_effects = StringVar()
        var_effects_value = StringVar()

        combobox = ttk.Combobox(self.items_frame, textvariable=countryvar)
        country.bind('<<ComboboxSelected>>', function)

        entry_attribute = ttk.Entry(self.items_frame, textvariable=var_attribute)
        entry_attribute_value = ttk.Entry(self.items_frame, textvariable=var_attribute_value)
        entry_action = ttk.Entry(self.items_frame, textvariable=var_action)
        entry_definitions = ttk.Entry(self.items_frame, textvariable=var_definitions)
        entry_needed_items = ttk.Entry(self.items_frame, textvariable=var_needed_items)
        entry_effects = ttk.Entry(self.items_frame, textvariable=var_effects)
        etnry_effects_value = ttk.Entry(self.items_frame, textvariable=var_effects_value)

        lbl_attribute = ttk.Label(self.items_frame, text='Attribute')
        lbl_attribute_value = ttk.Label(self.items_frame, text='Value')
        lbl_action = ttk.Label(self.items_frame, text='Action')
        lbl_definitions = ttk.Label(self.items_frame, text='Definition')
        lbl_needed_items = ttk.Label(self.items_frame, text='Needed Item Type')
        lbl_effects = ttk.Label(self.items_frame, text='Effect')
        lbl_effect_value = ttk.Label(self.items_frame, text='Value')

        button_attribute = ttk.Button(self.items_frame, text='add', command=add_attribute)
        button_action = ttk.Button(self.items_frame, text='add', command=add_attribute)
        button_definitions = ttk.Button(self.items_frame, text='add', command=add_attribute)
        button_attribute = ttk.Button(self.items_frame, text='add', command=add_attribute)
        button_attribute = ttk.Button(self.items_frame, text='add', command=add_attribute)
        button_attribute = ttk.Button(self.items_frame, text='add', command=add_attribute)

        


