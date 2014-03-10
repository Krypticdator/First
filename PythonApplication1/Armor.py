from Filecontrol import Filecontrol
from xml_file import xml_file
import xml.etree.ElementTree as ET
import math
class Armor(Filecontrol):
    """description of class"""
    def __init__(self, brand='', name='', price='', description='', ev=0, right_foot=0, right_hand=0, right_arm=0, right_leg=0, head=0, right_shlder=0, chest=0, vitals=0, stomach=0, left_shlder=0, thighs=0, left_leg=0, left_arm=0, left_hand=0, left_foot=0):
        self.__attributes={}
        self.__attributes['brand']=brand
        self.__attributes['name']=name
        self.__attributes['price']=price
        self.__attributes['description']=description
        self.__attributes['ev']=ev
        self.__attributes['full name'] = brand + ' ' + name
        self.__attributes['right_foot'] = right_foot
        self.__attributes['right_hand'] = right_hand
        self.__attributes['right_arm'] = right_arm
        self.__attributes['right_leg'] = right_leg
        self.__attributes['right_shlder'] = right_shlder
        self.__attributes['head'] = head
        self.__attributes['chest'] = chest
        self.__attributes['vitals'] = vitals
        self.__attributes['stomach'] = stomach
        self.__attributes['thighs'] = thighs
        self.__attributes['left_foot'] = left_foot
        self.__attributes['left_hand'] = left_hand
        self.__attributes['left_arm'] = left_arm
        self.__attributes['left_leg'] = left_leg
        self.__attributes['left_shlder'] = left_shlder
        
    
    def search_attributes(self, searched):
        file = xml_file()
        file.load_file('data/armors.xml')
        root = file.root
        for node in root.iter('armor'):
            brand = str(node.find('brand').text)
            name = str(node.find('name').text)
            if brand + ' ' + name == searched:
                type = str(node.find('type').text)
                cost = str(node.find('cost').text)
                ev_num = int(node.find('ev').text)
                sp_elements = list(node.find('sp'))
                self.add_attribute('type',type)
                self.add_attribute('cost',cost)
                self.add_attribute('ev',ev_num)
                for sp_value in sp_elements:
                    self.add_sp_location(sp_value.tag, sp_value.text)
            
    def add_attribute(self,attribute, value):
        self.__attributes[attribute] = value

    def add_sp_location(self, location, sp):
        try:
            self.__attributes[location] = int(sp)
        except Exception:
            self.__attributes[location] = 0

    def get_attribute(self, attribute):
        return self.__attributes[attribute]

    def get_sp_value(self, location):
        returned = 0
        try:
            returned = int(self.__attributes[location])
        except Exception:
            returned = 0
            print('error returning sp value of location, returning 0')
        return returned

class Effective_armor(Filecontrol):
    def __init__(self):
        super().__init__()
        self.read_file_to_segments('source/armor/hitlocations.txt', ';')
        self.sp= {}
        self.segmented_file_array.pop(7)
        self.bodyparts = {}
        self.armor_list = []
        for bodypart in self.segmented_file_array:
            self.bodyparts[bodypart[1]]=[]

    def add_armor(self, added_armor):
        print('add armor funktiossa')
        self.armor_list.append(added_armor)
        print('starting array creation in add_armor func)')
        print('name of added armor = ' + str(added_armor.get_attribute('full name')))
        print('parameter sp values = ' + str(added_armor._Armor__attributes))
        print(self.bodyparts)
        #double_prevention = []
        for bodypart, array in self.bodyparts.items():
            array.clear()
        print('done.. starting sp value retrieval')
        for armor in self.armor_list:
            for bodypart, array in self.bodyparts.items():
                try:
                    sp_value = int(armor.get_sp_value(bodypart))
                    print('sp value from armor ' + str(armor.get_attribute('full name')) + ' in location ' + str(bodypart) + ' reads as ' + str(sp_value))
                except Exception:
                    sp_value = 0
                    print('error handling bodypart: '  +str(bodypart))   
                if sp_value !=0:
                    #print('sp_value is other than 0, adding to array')
                    print('array consist of ' + str(array) + ' and added value is ' + str(sp_value))
                    array.append(sp_value)
                print('checking for doubles. array len is ' + str(len(array)) + ' and armor_list len is ' + str(len(self.armor_list)))
                if len(array)>len(self.armor_list):
                    print('destroying double armor')
                    array.pop(0)
            #double_prevention.append(armor.get_attribute('full name'))

        print('starting sp calculation process')
        print('bodyparts consist of following items: ' +str(self.bodyparts))
        for bodypart, array in self.bodyparts.items():
            print('going trough bodypart: ' + str(bodypart) + 'array looks like: ' +str(array))
            if len(array)!=0:
                base_sp = array[0]
                bonus = 0
                for i in range(1, len(array)):
                    bonus = self.calc_sp_layers(base_sp, array[i])
                    base_sp = base_sp + bonus
                    print('base_sp=' + str(base_sp))
                self.sp[bodypart] = base_sp
        print('finished sp calculations')
        print('self.sp:' + str(self.sp))
        print('armorlist: ' + str(self.armor_list))
       

                    

    def calc_sp_layers(self, sp1, sp2):
        ruletable = self.read_file_to_segments('source/armor/proportion_rules.txt',';', external_array=True)
        difference=0
        returned = 0
        try:
            sp1 = int(sp1)
        except Exception:
            print('sp1=' + str(sp1)+' ei konvertoitunut luvuksi')
            sp1 = 0
            
        try:
            sp2 = int(sp2)
        except Exception:
            sp2 = 0
            print('sp2 ei konvertoitunut luvuksi')
        
        valid = True
        if sp1!=0 and sp2!=0:
            difference = sp1 - sp2
            difference = int(math.fabs(difference))
            print('difference in sp:' + str(difference))
        else:
            valid = False
        
        '''print('first armorlayer check: ' + ruletable[0][0] + ' ' + ruletable[0][1])
        print('second armorlayer check: ' + ruletable[1][0] + ' ' + ruletable[1][1])
        print('third armorlayer check: ' + ruletable[2][0] + ' ' + ruletable[2][1])
        print('fourth armorlayer check: ' + ruletable[3][0] + ' ' + ruletable[3][1])
        print('fourth armorlayer check: ' + ruletable[4][0] + ' ' + ruletable[4][1])
        print('fourth armorlayer check: ' + ruletable[5][0] + ' ' + ruletable[5][1])'''
        
        #print('validation: ' + str(valid))
        #print('if difference equals or is greater than ' + str(ruletable[0][0]) + ' and is smaller or equal than ' + str(ruletable[0][1]))
        if int(difference) >= int(ruletable[0][0]) and int(difference) <= int(ruletable[0][1]) and valid:
            returned = int(ruletable[0][2])
        #    print('1. if lause armor_calcissa, lopputuloksena: ' +str(returned))

        elif int(difference) >= int(ruletable[1][0]) and int(difference) <= int(ruletable[1][1])and valid:
            returned = int(ruletable[1][2])
        #    print('2. if lause armor_calcissa, lopputuloksena: ' +str(returned))

        elif difference >= int(ruletable[2][0]) and difference <= int(ruletable[2][1])and valid:
            returned = int(ruletable[2][2])
        #    print('3. if lause armor_calcissa, lopputuloksena: ' +str(returned))

        elif difference >= int(ruletable[3][0]) and difference <= int(ruletable[3][1])and valid:
            returned = int(ruletable[3][2])
        #    print('4. if lause armor_calcissa, lopputuloksena: ' +str(returned))   

        elif difference >= int(ruletable[4][0]) and difference <= int(ruletable[4][1])and valid:
            returned = int(ruletable[4][2])
        #    print('5. if lause armor_calcissa, lopputuloksena: ' +str(returned))   

        elif difference >= int(ruletable[5][0]) and difference <= int(ruletable[5][1])and valid:
            returned = int(ruletable[5][2])
        #    print('6. if lause armor_calcissa, lopputuloksena: ' +str(returned))   

        #returned = sp1 + returned
        #print('final sp in calculations' + str(returned))
        #print('bonus according to armor convert talbe is: ' + str(returned))
        return returned



        


