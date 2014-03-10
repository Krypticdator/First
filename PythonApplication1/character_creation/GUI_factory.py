from tkinter import *
from tkinter import ttk
from GUI_header import GUI_header
class GUI_factory(object):
    """description of class"""

class Category_UI(object):
    def __init__(self, master, controller='none', frametext = 'default', first_header='Categories', second_header='list', third_header='Description', category_width=25, category_height=10, list_width = 25, list_height=10, desc_width=40, desc_height=10):
        self.contr = controller
        self.frame = ttk.Labelframe(master, text=frametext)
        self.p = ttk.Panedwindow(self.frame, orient=HORIZONTAL)
        self.p2 = ttk.Panedwindow(self.frame, orient=HORIZONTAL)

        self.last_category_selection = 0
        self.last_list_selection = 0
        
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

        self.box_categories = Listbox(self.f1, height=category_height, width=category_width)
        self.box_list = Listbox(self.f2, height=list_height, width=list_width)
        self.text_description = Text(self.f3, width=desc_width, height=desc_height, wrap = 'word')
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
        self.header = GUI_header(self.frame, self.contr)

        self.frame.grid(column=0, row=0)
        self.header.frame.grid(column=0, row=0)
        self.p.grid(column = 0, row = 1)
        self.p2.grid(column = 0, row = 2, sticky=(W))
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
        '''fills the listbox with items in the list, automatically sorts them
        if filepath is none, uses provided list'''
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
        try:
            id = self.box_categories.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.last_category_selection
        self.last_category_selection=luku
        values = []

        for avain, arvo in self.categories_and_items.items():
            if str.casefold(arvo)==str.casefold(self.box_categories.get(luku)):
                #self.box_list.insert(END, avain)
                values.append(avain)
        values.sort()

        for avain in values:
            self.box_list.insert(END, avain)
        

    def show_text(self, *args):
        try:
            id = self.box_list.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.last_list_selection
        self.last_list_selection=luku
        self.text_description.delete(1.0, 'end')
        text = self.list_items_and_descriptions[self.box_list.get(luku)]
        self.text_description.insert(1.0, text)

    def add_category_items(self, category, list):
        '''puts all provided list items under the provided category'''
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
        '''Collects all added categories from categories_and_items dictionary
        sorts categorylist when ready'''
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
                #print('rivitiedot len is ' + str(len(rivitiedot)))
                if len(rivitiedot)==5:
                    value = rivitiedot[1]
                    frequency = rivitiedot[2]
                    intensity = rivitiedot[3]
                    importance = rivitiedot[4]
                    comp = True
                    self.contr.set_to_ability_list(self.name, key, value , comp, frequency, intensity, importance)
                else:
                    value = rivitiedot[1]
                #print(merkkijono + ' ' + key + ' ' + value)
                    self.contr.set_to_ability_list(self.name, key, value)
            except Exception:
                #print('whupsee')
                print(self.contr._Controller__char.get_ability_list(self.name))

        #self.contr.print_all_abilities()
        self.contr.recalculate_points()
        self.text_inventory.edit_modified(False)
        d.close()

    def add_to_inventory(self, *args):
        try:
            id = self.box_list.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.last_list_selection
        text = self.box_list.get(luku)
        self.contr.set_to_ability_list(self.name, text, 1)
        #list = self.contr.get_from_ability_list(self.name)
        #value = self.contr.get_char_skill(text)
        value = self.contr.get_from_ability_list(self.name, text)

        text = text + '\t\t\t\t|' + str(value) + '\n'
        self.text_inventory.insert('end', text)

class textbox(object):
    def __init__(self, master, header, width_num, height_num, column_num=0, row_num=0):
        self.frame = ttk.LabelFrame(master, text=header)
        self.box = Text(self.frame, width=width_num, height=height_num, wrap = 'word')
        s1 = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.box.yview)
        self.box['yscrollcommand'] = s1.set
        self.frame.grid(column=column_num, row=row_num)
        self.box.grid(column = 0, row=0)
        s1.grid(column = 1, row = 0, sticky=(N,S))
    def new_text(self, text):
        self.box.delete(1.0, 'end')
        self.box.insert(1.0, text)

class text_and_inputfield:
    def __init__(self, master, topic, variable, width_label=15, width_num=2):
        self.frame = ttk.Frame(master)
        self.textlabel = ttk.Label(self.frame, text=topic,width=width_label)
        self.entry = ttk.Entry(self.frame, textvariable=variable, width=width_num)
        self.variable = variable

        self.frame.grid(column = 0, row = 0)
        self.textlabel.grid(column=0, row=0 )
        self.entry.grid(column=1, row=0)

class radio_group(object):
    def __init__(self, master, choices, label, checkboxes=False, row_num=0, column_num=0, info_text_line=False, info_text_length=20, rowspan_num=1, columnspan_num=1):
        #print('created radio_group')
        self.frame = ttk.LabelFrame(master, text=label)
        self.header = label
        self.variable = StringVar()
        self.buttons = {}
        self.rowspan_num = rowspan_num

        if checkboxes:
            self.variables = {}
            for choice in choices:
                x = StringVar()
                x.set('off')
                self.variables[choice]=x
                self.buttons[choice] = ttk.Checkbutton(self.frame, text=choice, command=self.value_changed, variable=self.variables[choice], onvalue='on', offvalue='off')
        else:
            for choice in choices:
                self.buttons[choice] = ttk.Radiobutton(self.frame, text=choice, variable=self.variable, value=choice, command=self.calc)
        
        if info_text_line:
            self.label_variables = {}
            self.info_labels = {}
            for choice in choices:
                x = StringVar()
                self.label_variables[choice] = x
                self.info_labels[choice] = ttk.Label(self.frame, textvariable = self.label_variables[choice], width = info_text_length)
        
        #print(str(rowspan_num))
        self.frame.grid(column=column_num, row=row_num,rowspan=self.rowspan_num, columnspan=columnspan_num, sticky=(N, W))
        list_row_num = 0
        list_column_num=0
        choices.sort()
        for choice in choices:
            for key, value in self.buttons.items():
                if key==choice:
                    value.grid(column=list_column_num, row=list_row_num, sticky=(W))
                    if info_text_line:
                        self.info_labels[choice].grid(column=list_column_num +1, row=list_row_num, sticky=(W))
                    list_row_num = list_row_num +1

    def value_changed(self):
        pass

    def calc(self):
        pass

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


class CustomText(Text):
    '''A text widget with a new method, HighlightPattern 

    example:

    text = CustomText()
    text.tag_configure("red",foreground="#ff0000")
    text.HighlightPattern("this should be red", "red")

    The highlight_pattern method is a simplified python 
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular expression
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart",start)
        self.mark_set("matchEnd",start)
        self.mark_set("searchLimit", end)

        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index,count.get()))
            self.tag_add(tag, "matchStart","matchEnd")





