from tkinter import *
from tkinter import ttk
class GUI_factory(object):
    """description of class"""

class Category_UI(object):
    def __init__(self, master, controller='none', frametext = 'default', first_header='Categories', second_header='list', third_header='Description'):
        self.contr = controller
        self.frame = ttk.Labelframe(master, text=frametext)
        self.p = ttk.Panedwindow(self.frame, orient=HORIZONTAL)
        self.p2 = ttk.Panedwindow(self.frame, orient=HORIZONTAL)
        
        self.name = str.lower(frametext)
        self.inventory_file="data/" + self.name + "_inventory.txt"
        self.categories_and_items = {}
        self.list_items_and_descriptions = {}

        self.f1 = ttk.Labelframe(self.p, text=first_header,  width=100,  height=100)
        self.f2 = ttk.Labelframe(self.p, text=second_header, width=100,  height=100)
        self.f3 = ttk.Labelframe(self.p, text=third_header,  width=100,  height=100)
        self.f4 = ttk.Labelframe(self.p2, text='You have:', width=100, height=100)

        self.p.add(self.f1)
        self.p.add(self.f2)
        self.p.add(self.f3)
        self.p2.add(self.f4)

        self.box_categories = Listbox(self.f1, height=10, width=25)
        self.box_list = Listbox(self.f2, height=10, width=25)
        self.text_description = Text(self.f3, width=40, height=10, wrap = 'word')
        self.button_add = ttk.Button(self.f3,text="Add", command=self.add_to_inventory)
        self.text_inventory = Text(self.f4, width=40, height=10, wrap='word')

        s1 = ttk.Scrollbar(self.f1, orient=VERTICAL, command=self.box_categories.yview)
        s2 = ttk.Scrollbar(self.f2, orient=VERTICAL, command=self.box_list.yview)
        s3 = ttk.Scrollbar(self.f3, orient=VERTICAL, command=self.text_description.yview)
        s4 = ttk.Scrollbar(self.f4, orient=VERTICAL, command=self.text_inventory.yview)

        self.box_categories['yscrollcommand'] = s1.set
        self.box_list['yscrollcommand'] = s2.set
        self.text_description['yscrollcommand'] = s3.set
        self.text_inventory['yscrollcommand'] = s4.set

        self.box_categories.bind('<<ListboxSelect>>', self.show_list)
        self.box_list.bind('<<ListboxSelect>>', self.show_text)
        self.text_inventory.bind('<<Modified>>', self.inventory_changed)

        self.frame.grid(column=0, row=0)
        self.p.grid(column = 0, row = 0)
        self.p2.grid(column = 0, row = 1, sticky=(W))
        self.box_categories.grid(column = 0, row = 0)
        self.box_list.grid(column = 0, row = 0)
        self.text_description.grid(column = 0, row = 0)
        self.button_add.grid(column = 2, row = 0, sticky = (N))
        self.text_inventory.grid(column = 0, row = 0)
        s1.grid(column = 1, row = 0, sticky=(N,S))
        s2.grid(column = 1, row = 0, sticky = (N, S))
        s3.grid(column = 1, row = 0, sticky = (N, S))
        s4.grid(column = 1, row = 0, sticky = (N, S))

    def populate_box(self, box, list, filepath='none'):
        if filepath == 'none':
            list.sort()
            for item in list:
                box.insert(END, item)
            box.selection_set(0)
        else:
            self.contr.settings.Read_file(filepath, list)
            list.sort()
            for item in list:
                box.insert(END, item)
            box.selection_set(0)

    def show_list(self, *args):
        self.box_list.delete(0, END)
        id = self.box_categories.curselection()
        luku = int(id[0])
        values = []

        for avain, arvo in self.categories_and_items.items():
            if arvo==self.box_categories.get(luku):
                #self.box_list.insert(END, avain)
                values.append(avain)
        values.sort()

        for avain in values:
            self.box_list.insert(END, avain)
        

    def show_text(self, *args):
        id = self.box_list.curselection()
        luku = int(id[0])
        self.text_description.delete(1.0, 'end')
        text = self.list_items_and_descriptions[self.box_list.get(luku)]
        self.text_description.insert(1.0, text)

    def add_category_items(self, category, list):
        for item in list:
            self.categories_and_items[item] = category

    def set_dictionaries(self, filepath_categories='empty', filepath_descriptions='empty', sep=';'):
        if filepath_categories=='empty':
            pass
        else:
            self.read_to_dictionary(filepath_categories, self.categories_and_items, key_value=False, separator=sep)

        if filepath_descriptions=='empty':
            pass
        else:
            self.read_to_dictionary(filepath_descriptions, self.list_items_and_descriptions, separator=sep)

    def collect_categories(self):
        categories = []
        for key, value in self.categories_and_items.items():
            if value in categories:
                pass
            else:
                categories.append(value)
        categories.sort()
        return categories

    def read_to_dictionary(self, filepath, dictionary, key_value=True, separator = ';'):
        f = open(filepath, 'r')
        for line in f:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(separator, -1)
            #print(rivitiedot)
            if key_value:
                dictionary[rivitiedot[0]] = rivitiedot[1]
            else: #value-key
                dictionary[rivitiedot[1]] = rivitiedot[0]
        f.close()

    def inventory_changed(self, *args):
        #flag = self.text_inventory.edit_modified()
        #print(flag)
        f = open(self.inventory_file, 'w+')
        f.write(self.text_inventory.get(1.0, 'end'))
        f.close()

        self.contr.clear_ability_list(self.name)

        d= open(self.inventory_file, 'r')
        for line in d:
            merkkijono = line[:-1]
            try: 
                #merkkijono = line
                rivitiedot = merkkijono.split('|', -1)
                key = str.strip(rivitiedot[0])
                value = rivitiedot[1]
                #print(merkkijono + ' ' + key + ' ' + value)
                self.contr.set_to_ability_list(self.name, key, value)
            except Exception:
                #print('whupsee')
                print(self.contr._Controller__char.get_ability_list(self.name))

        #self.contr.print_all_abilities()
        self.text_inventory.edit_modified(False)

    def add_to_inventory(self, *args):
        id = self.box_list.curselection()
        luku = int(id[0])
        text = self.box_list.get(luku)
        value = self.contr.get_char_skill(text)

        text = text + '\t\t\t\t|' + str(value) + '\n'
        self.text_inventory.insert('end', text)



