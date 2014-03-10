from GUI_factory import Category_UI
from Filecontrol import Filecontrol
from tkinter import *
from tkinter import ttk
from Armor import Effective_armor
class GUI_armor(Category_UI):
    """description of class"""
    def __init__(self, master, controller = 'none', frametext = 'Armor', first_header = 'Categories', second_header = 'Available', third_header = 'Description'):
        super().__init__(master, controller, frametext, first_header, second_header, third_header)
        self.extract_categories()
        self.text_description.destroy()
        self.armorbox = armorBox(self.p, controller)
        self.p.add(self.armorbox.frame)
        self.e_armor = Effective_armor()
      
    def extract_categories(self):
        #print('extract armors')
        #print(self.contr.settings.armors)
        for armor in self.contr.settings.armors:
            #print('extract armors loop')
            #print(self.contr.settings.armors)
            brand = armor.get_attribute('brand')
            name = armor.get_attribute('name')
            self.categories_and_items[brand + ' ' + name] = brand
        #print(self.categories_and_items)

        categories = self.collect_categories()
        self.populate_box(self.box_categories,categories)

    def show_text(self, *args):
        try:
            id = self.box_list.curselection()
            luku = int(id[0])
        except Exception:
            luku = self.last_list_selection
        
        category_luku = self.last_category_selection

        for armor in self.contr.settings.armors:
            if armor.get_attribute('brand')==self.box_categories.get(category_luku):
                #print('past the first if statement in armor sp retrieval')
                #print(armor.get_attribute('name'))

                #print(self.box_list.get(luku))
                full_name = armor.get_attribute('brand') + " " + armor.get_attribute('name')
                if full_name==self.box_list.get(luku):
                    #print('past the second if statement in armor sp retrieval')
                    for loc in self.armorbox.segmented_file_array:
                        bodypart_name = loc[1]
                        #self.armorbox.variables[bodypart_name].set(armor.get_attribute(bodypart_name))
                        #print(self.armorbox.variables[bodypart_name].get())
                        if int(self.armorbox.variables[bodypart_name].get()) == 0:
                            self.armorbox.added_variables[bodypart_name].set('+' + str(armor.get_sp_value(bodypart_name)))
                        else:
                            #print('else lauseessa')
                            e = Effective_armor()
                            layer1=self.armorbox.variables[bodypart_name].get()
                            #print('layer1' + layer1)
                            layer2=armor.get_sp_value(bodypart_name)
                            bonus = e.calc_sp_layers(layer1, layer2)
                            self.armorbox.added_variables[bodypart_name].set('+' + str(bonus))

    def inventory_changed(self, *args):
        #flag = self.text_inventory.edit_modified()
        #print(flag)
        f = open(self.inventory_file, 'w+')
        f.write(self.text_inventory.get(1.0, 'end'))
        f.close()
        e = Effective_armor()
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
                for armor in self.contr.settings.armors:
                    #print('armorfinding: ' + key + ' ' + armor.get_attribute('full name'))
                    if key == armor.get_attribute('full name'):
                        #print('armorfinding succeeded')
                        e.add_armor(armor)
                
            except Exception:
                #print('whupsee')
                print(self.contr._Controller__char.get_ability_list(self.name))
        
        for key, element in self.armorbox.variables.items():
            #print(e.sp)
            try:
                element.set(e.sp[key])
            except Exception:
                element.set('0')
        #print('armorlist pituus' +str(len(e.armor_list)))
        #self.contr.print_all_abilities()
        self.show_text()
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

        armor = self.contr.settings.get_armor(text)
        cost = armor.get_attribute('price')
        

        self.contr.set_to_ability_list(self.name, text, cost)
        #list = self.contr.get_from_ability_list(self.name)
        #value = self.contr.get_char_skill(text)
        value = self.contr.get_from_ability_list(self.name, text)

        text = text + '\t\t\t\t|' + str(value) + '\n'
        self.text_inventory.insert('end', text)


    
                    

class armorBox(Filecontrol):
    def __init__(self, master, controller):
        super().__init__()
        self.read_file_to_segments('source/armor/hitlocations.txt',';')
        self.segmented_file_array.pop(7)
        self.frame = ttk.Labelframe(master, text="Protection", width=100,  height=100)
        self.contr = controller

        self.labels = {}
        self.v_labels = {}
        self.variables = {}
        self.added_v_labels = {}
        self.added_variables = {}

        for location in self.segmented_file_array:
            self.labels[location[1]] = ttk.Label(self.frame, text=location[1])
            self.variables[location[1]] = StringVar()
            self.variables[location[1]].set('0')
            self.added_variables[location[1]] = StringVar()
            self.v_labels[location[1]] = ttk.Label(self.frame, textvariable=self.variables[location[1]], width=3) 
            self.added_v_labels[location[1]] = ttk.Label(self.frame, textvariable=self.added_variables[location[1]], width=3)

        column_num = 0
        row_num = 0
        self.frame.grid(column=0, row=0)

        for location in self.segmented_file_array:
            for key, value in self.labels.items():
                if location[1] == key:
                    value.grid(column = column_num, row=row_num)
                    row_num = row_num +1

        column_num = 1
        row_num = 0

        for location in self.segmented_file_array:
            for key, value in self.v_labels.items():
                if location[1] == key:
                    value.grid(column = column_num, row=row_num)
                    row_num = row_num +1

        column_num = 2
        row_num = 0
        for location in self.segmented_file_array:
            for key, value in self.added_v_labels.items():
                if location[1] == key:
                    value.grid(column = column_num, row=row_num)
                    row_num = row_num +1