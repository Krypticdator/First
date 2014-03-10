from tkinter import *
from tkinter import ttk
from GUI_factory import radio_group
from GUI_factory import textbox
from GUI_factory import CustomText
from cyberitem import cyberitem as cp_item
class GUI_cyber(object):
    """description of class"""
    def __init__(self, master, controller):
        self.contr = controller
        self.frame = ttk.Labelframe(master, text="cybernetics")
        cybertypelist=[]
        cybertypelist.append("Fashionware")
        cybertypelist.append("Neuralware")
        cybertypelist.append("Implants")
        cybertypelist.append("Bioware")
        cybertypelist.append("Cyberweapons")
        cybertypelist.append("Cyberoptic")
        cybertypelist.append("Cyberaudio")
        cybertypelist.append("Cyberarm")
        cybertypelist.append("Cyberleg")
        cybertypelist.append("Bodyplating")
        cybertypelist.append("Chipware")
        self.box = textbox(self.frame, "your operation details", 40, 10, 0, 2)
        self.button = ttk.Button(self.frame, text='Take the operation', command=self.make_operation)
        self.button.grid(row=3, column=0)
        self.menu_dictionary = {}
        self.menu_list = []
        self.leg_list = []
        self.bioware_list = []
        self.neuralware_list = []
        self.bodyplating_list = []
        self.cyberaudio_list = []
        self.bodyweapons_list = []
        self.cyberoptic_list = []
        self.implants_list = []
        self.fashionware_list = []
        self.chipware_list = []
        self.menu_dictionary['Cyberarm'] = self.menu_list
        self.menu_dictionary['Cyberleg'] = self.leg_list
        self.menu_dictionary['Bioware'] = self.bioware_list
        self.menu_dictionary['Neuralware'] = self.neuralware_list
        self.menu_dictionary['Bodyplating'] = self.bodyplating_list
        self.menu_dictionary['Cyberaudio'] = self.cyberaudio_list
        self.menu_dictionary['Cyberweapons'] = self.bodyweapons_list
        self.menu_dictionary['Cyberoptic'] = self.cyberoptic_list
        self.menu_dictionary['Implants'] = self.implants_list
        self.menu_dictionary['Fashionware'] = self.fashionware_list
        self.menu_dictionary['Chipware'] = self.chipware_list

        self.cybertypes = cyberware_radio_group(self.frame, cybertypelist, "Choose type", controller=self.contr, textbox=self.box, all_menus=self.menu_list)
        self.cybertypes.frame.grid_remove()
        self.starter = cybertype_start_menu(self.frame, cybertypelist, "Choose type", menu_dictionary = self.menu_dictionary, rowspan_num=2)
       
        
        self.cyberlimb_required = self.cybertypes.create_sub_menu("cyberlimbs", "required", 0, 1, self.menu_list)
        self.cyberlimb_options = self.cybertypes.create_sub_menu("cyberlimb options", "cyberarm options", 1, 1, self.menu_list)
        self.cyberhand_options = self.cybertypes.create_sub_menu("cyberhands", "cyberhand options", 2, 1, self.menu_list)
        self.cyberweapons_options = self.cybertypes.create_sub_menu("cyberweapons", "weapons", 0, 2, self.menu_list)
        self.buildin_options = self.cybertypes.create_sub_menu("buildins", "build-ins",1, 2, self.menu_list)

        self.cyberlimb_required2 = self.cybertypes.create_sub_menu("cyberlimbs", "required", 0, 1, self.menu_list)
        self.cyberlimb_options2 = self.cybertypes.create_sub_menu("cyberlimb options", "cyberleg options", 1, 1, self.leg_list)
        self.cyberhand_options2 = self.cybertypes.create_sub_menu("cyberfeet", "cyberfeet options", 2, 1, self.leg_list)
        self.cyberweapons_options2 = self.cybertypes.create_sub_menu("cyberweapons", "weapons", 0, 2, self.leg_list)
        self.buildin_options2 = self.cybertypes.create_sub_menu("buildins", "build-ins",1, 2, self.leg_list)

        self.bioware = self.cybertypes.create_sub_menu('bioware', 'bioware',0,1,self.bioware_list)
        self.neuralware_req = self.cybertypes.create_sub_menu('required','required',0,1,self.neuralware_list)
        self.neuralware = self.cybertypes.create_sub_menu('Neuralware', 'neuralware',1,1,self.neuralware_list)
        self.bodyplating = self.cybertypes.create_sub_menu('bodyplating', 'bodyplating',0,1,self.bodyplating_list)
        self.cyberaudio_required = self.cybertypes.create_sub_menu('cyberaudio', 'required', 0,1,self.cyberaudio_list)
        self.cyberaudio = self.cybertypes.create_sub_menu('cyberaudio options', 'cyberaudio',1,1,self.cyberaudio_list)
        self.cyberweapon = self.cybertypes.create_sub_menu('bodyweapons', 'cyberweapons',0,1,self.bodyweapons_list)
        self.cyberoptics_required = self.cybertypes.create_sub_menu('cyberoptics', 'required',0,1,self.cyberoptic_list)
        self.cyberoptics = self.cybertypes.create_sub_menu('cyberoptic options', 'cyberoptics',1,1,self.cyberoptic_list)
        self.implants = self.cybertypes.create_sub_menu('implants', 'implants',0,1,self.implants_list)
        self.fashionware = self.cybertypes.create_sub_menu('fashionware', 'fashionware', 0,1,self.fashionware_list)
        self.chipware = self.cybertypes.create_sub_menu('chipware', 'chipware', 0,1,self.chipware_list)
      
        self.menu_list.append(self.cyberlimb_options)
        self.menu_list.append(self.cyberhand_options)
        self.menu_list.append(self.cyberweapons_options)
        self.menu_list.append(self.buildin_options)
        self.menu_list.append(self.cyberlimb_required)

        self.leg_list.append(self.cyberlimb_options2)
        self.leg_list.append(self.cyberhand_options2)
        self.leg_list.append(self.cyberweapons_options2)
        self.leg_list.append(self.buildin_options2)
        self.leg_list.append(self.cyberlimb_required2)

        self.bioware_list.append(self.bioware)
        self.neuralware_list.append(self.neuralware_req)
        self.neuralware_list.append(self.neuralware)
        self.bodyplating_list.append(self.bodyplating)
        self.cyberaudio_list.append(self.cyberaudio)
        self.cyberaudio_list.append(self.cyberaudio_required)
        self.bodyweapons_list.append(self.cyberweapon)
        self.cyberoptic_list.append(self.cyberoptics)
        self.cyberoptic_list.append(self.cyberoptics_required)
        self.implants_list.append(self.implants)
        self.fashionware_list.append(self.fashionware)
        self.chipware_list.append(self.chipware)

    def make_operation(self):
        total_hum_cost = 0
        root_cyberwear = cp_item(name='default')
        installed_options = []
        #print(self.menu_dictionary)
        for menu_name, array in self.menu_dictionary.items():
            for cell in array:
                #print(array)
                #print(str(key) + " + " + str(value.get()))
                for key, value in cell.variables.items():
                    if value.get()=='on':
                        #print('here I am LJ')
                        cyberitem = self.contr.settings.get_cyber(key)
                        cost = cyberitem.calc_effective_hum_cost()
                        total_hum_cost = total_hum_cost + cost
                        if cell.header=='required':
                            root_cyberwear = cyberitem
                        else:
                            installed_options.append(cyberitem)
                        value.set('off')
                        #print(str(cost))
        for cyberwear in installed_options:
            root_cyberwear.add_installed_option(cyberwear)
        #print(str(root_cyberwear))
        #print(installed_options)
        #print(str(total_hum_cost))
        self.contr.set_to_ability_list('cyberwear',root_cyberwear, 0)
        self.show_installed_cyberwear()

    def show_installed_cyberwear(self):
        self.window = Toplevel(self.frame)
        frame = ttk.Labelframe(self.window, text='installed cyberwear')
        cyberwears = self.contr.get_char_cyberwear()
        nameframe = ttk.Labelframe(frame, text='name')
        descframe = ttk.Labelframe(frame, text='description')
        humframe = ttk.LabelFrame(frame, text='h. loss')
        costframe = ttk.LabelFrame(frame, text='dcd')
        total_cost = 0
        total_hum = 0
        column_num=0
        row_num=0
        for cyber in cyberwears:
            label = ttk.Label(nameframe, text=cyber.get_attribute('name'))
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        column_num=0
        row_num=0
        for cyber in cyberwears:
            label = ttk.Label(descframe, text=cyber.get_attribute('description_short'))
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        column_num=0
        row_num=0
        for cyber in cyberwears:
            label = ttk.Label(humframe, text=cyber.get_attribute('effective_hum_cost'))
            total_hum = total_hum + int(cyber.get_attribute('effective_hum_cost'))
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        column_num=0
        row_num=0
        for cyber in cyberwears:
            label = ttk.Label(costframe, text=cyber.get_attribute('cost'))
            total_cost = total_cost + int(cyber.get_attribute('cost'))
            label.grid(column=column_num, row=row_num, sticky=(W))
            row_num=row_num +1

        rof_num = row_num +1
        total_hum_label = ttk.Label(frame, text='Total h. loss')
        total_hum_v_label = ttk.Label(frame, text=str(total_hum))
        total_cost_label = ttk.Label(frame, text='Total dcd cost')
        total_cost_v_label = ttk.Label(frame, text=str(total_cost))

        frame.grid(column=0, row=0)
        nameframe.grid(column=0, row=0)
        descframe.grid(column=1, row=0)
        humframe.grid(column=2, row=0)
        costframe.grid(column=3, row=0)
        total_hum_label.grid(column=0, row=1, sticky=(W))
        total_hum_v_label.grid(column=1, row=1, sticky=(W))
        total_cost_label.grid(column=0, row=2, sticky=(W))
        total_cost_v_label.grid(column=1, row=2, sticky=(W))

        
class cybertype_start_menu(radio_group):
    def __init__(self, master, choices, label, checkboxes = False, row_num = 0, column_num = 0, info_text_line = False, info_text_length = 30, menu_dictionary={}, rowspan_num=1):
        super().__init__(master, choices, label, checkboxes, row_num, column_num, info_text_line, info_text_length, rowspan_num)
        self.dictionary = menu_dictionary
    
    def calc(self):
        for key, array in self.dictionary.items():
            for cell in array:
                cell.frame.grid_remove()
        for cell in self.dictionary[self.variable.get()]:
            cell.frame.grid()

class cyberware_radio_group(radio_group):
    def __init__(self, master, choices, label, checkboxes = False, row_num = 0, column_num = 0, controller = object, second_line=False, line_len=30, textbox = object, all_menus=[]):
        super().__init__(master, choices, label, checkboxes, row_num, column_num, second_line, line_len)
        self.contr = controller
        self.master = master
        self.box = textbox
        self.all_menus = all_menus

        

    def calc(self):
        '''for menu in self.all_menus:
            menu.frame.grid()    

        #if self.variable.get() == "Cyberarm":
            #print("Calc funktion if lauseessa")
            self.cyberlimb_options.frame.grid()
            self.cyberhand_options.frame.grid()
            self.cyberweapons_options.frame.grid()
            self.buildin_options.frame.grid()'''

        
    def value_changed(self):
        
        info_text=''
        info_text2=''
        description = ''
        hum_cost_estimate_min = 0
        hum_cost_estimate_max = 0
        total_cost = 0
        #print('value changed funktio alkaa')
        #print(str(self.all_menus))
        for menu in self.all_menus:
            #print('loop of all menus')
            #print(menu.header)
            for key, value in menu.variables.items():
                #print('second loop ' + str(key) + ' '+ str(value) +' '+ str(value.get()))
                if value.get()=='on':
                    #print('Key is '+key)
                    cyberitem = self.contr.settings.get_cyber(key)
                    if cyberitem.get_attribute('description_long')!='undefined':
                        description =  description + cyberitem.get_attribute('description_long') + '\n\n'

                    if menu.header == 'required':
                        info_text = key + '(' + info_text2 + ')'
                    else:
                        info_text2 = info_text2 + key + ', '
                    hum_cost_estimate_min = hum_cost_estimate_min + cyberitem.get_attribute('hum_cost_min')
                    hum_cost_estimate_max = hum_cost_estimate_max + cyberitem.get_attribute('hum_cost_max')
                    total_cost = total_cost + int(cyberitem.get_attribute("cost"))
                    #info_text = info_text + key +'\n'
        final_text=''
        if info_text == '':
            final_text = info_text2 + '\n\n' + description      
        else:
            final_text = info_text + '\n\n' +description
       
        money_text = "Cost: " + str(total_cost) + '\n'
        hum_text = "Humanity cost: " + str(hum_cost_estimate_min) + "-" + str(hum_cost_estimate_max) + "\n"
        final_text =money_text + hum_text + final_text
        self.box.new_text(final_text)
        
        #print('info text is ' + info_text)

    def create_sub_menu(self, category, header, row_num, column_num, menu):
        options = []
        info_text = {}
        for cyberobject in self.contr.settings.cybers:
            if cyberobject.get_attribute('category')==category:
                options.append(cyberobject.get_attribute('name'))
                info_text[cyberobject.get_attribute('name')] = cyberobject.get_attribute('description_short')
        popup_list = cyberware_radio_group(self.master, options, header, True, row_num, column_num, self.contr, True, 40, self.box, all_menus=menu)
        for option in options:
            popup_list.label_variables[option].set(info_text[option])
        popup_list.frame.grid_remove()
        return popup_list
            



