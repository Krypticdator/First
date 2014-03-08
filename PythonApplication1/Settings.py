from Weapon import Weapon
from Armor import Armor
from cyberitem import cyberitem
from Filecontrol import Filecontrol
import random
import copy
from xml_file import xml_file
import xml.etree.ElementTree as ET
class Settings(Filecontrol):
    """description of class"""

    def __init__(self):
        self.wpn_classes = []
        self.light_pistols = []
        self.medium_pistols = []
        self.heavy_pistols = []
        self.v_heavy_pistols = []
        self.l_submachineguns = []
        self.m_submachineguns = []
        self.h_submachineguns = []
        self.shotguns = []
        self.a_rifles = []
        self.s_rifles = []
        self.o_rifles = []
        self.machineguns = []
        self.failed_wpns = []
        self.all_weapons = {}
        self.skill_categories = []
        self.quality_rating = {}
        self.armors = []
        self.cybers = []
        self.cyber_descr_long = {}

        
        self.success_wpns = 0
        self.failure_wpns = 0

        self.attribute_descriptions = {}

        #self.Read_file('source/descr_attries.txt', self.attribute_descriptions)
        self.read_to_dictionary('source/descr_attries.txt',self.attribute_descriptions, True, '_')

        self.Read_file('source/wpns/weapon_classes.txt', self.wpn_classes) 
        self.Read_wpn('source/wpns/l_pistols.txt', self.light_pistols)
        self.Read_wpn('source/wpns/m_pistols.txt', self.medium_pistols)
        self.Read_wpn('source/wpns/h_pistols.txt', self.heavy_pistols)
        self.Read_wpn('source/wpns/v_h_pistols.txt', self.v_heavy_pistols)
        self.Read_wpn('source/wpns/l_submachineguns.txt', self.l_submachineguns)
        self.Read_wpn('source/wpns/m_submachineguns.txt', self.m_submachineguns)
        self.Read_wpn('source/wpns/h_submachineguns.txt', self.h_submachineguns)
        self.Read_wpn('source/wpns/shotguns.txt', self.shotguns)
        self.Read_wpn('source/wpns/assault_rifles.txt', self.a_rifles)
        self.Read_wpn('source/wpns/s_rifles.txt', self.s_rifles)
        self.Read_wpn('source/wpns/o_rifles.txt', self.o_rifles)
        self.Read_wpn('source/wpns/machineguns.txt', self.machineguns)

        self.read_armors('data/armors.xml', self.armors)

        self.read_cyber('source/cyberware/bioware.txt')
        self.read_cyber('source/cyberware/bodyplating.txt')
        self.read_cyber('source/cyberware/bodyskulpting.txt')
        self.read_cyber('source/cyberware/bodyweapons.txt')
        self.read_cyber('source/cyberware/buildins.txt')
        self.read_cyber('source/cyberware/chipware.txt')
        self.read_cyber('source/cyberware/cyberaudio.txt')
        self.read_cyber('source/cyberware/cyberaudio_options.txt')
        self.read_cyber('source/cyberware/cyberfeet.txt')
        self.read_cyber('source/cyberware/cyberhands.txt')
        self.read_cyber('source/cyberware/cyberlimb_options.txt')
        self.read_cyber('source/cyberware/cyberlimbs.txt')
        self.read_cyber('source/cyberware/cyberoptics.txt')
        self.read_cyber('source/cyberware/cyberoptics_options.txt')
        self.read_cyber('source/cyberware/cyberweapons.txt')
        self.read_cyber('source/cyberware/fashionware.txt')
        self.read_cyber('source/cyberware/implants.txt')
        self.read_cyber('source/cyberware/nanotech.txt')
        self.read_cyber('source/cyberware/neuralware.txt')
        self.read_cyber('source/cyberware/voice.txt')
        self.read_cyber('source/cyberware/neuralware_req.txt')

        self.load_cyber_descr_long()
        self.set_cyber_descr_long()
        x = cyberitem(name="default")
        self.cybers.append(x)
        

        self.Read_quality_rating('source/quality_rating.txt')

        print(self.success_wpns)
        print(self.failure_wpns)


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

    def Read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

    def Read_quality_rating(self, filepath):
        f = open(filepath, 'r')
        for line in f:
            merkkijono = line.strip()
            rivitiedot = merkkijono.split(";", -1)
            i = int(rivitiedot[1])
            end = int(rivitiedot[2])
            for i in range(i, end):
                self.quality_rating[i] = rivitiedot[0]


    def Read_wpn(self, filepath, target):
        d = open(filepath, 'r')
        for line in d:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(";", -1)
            wpn = Weapon()

            wpn.addAttribute("Name", rivitiedot[0])
            wpn.addAttribute("Type", rivitiedot[1])
            wpn.addAttribute("WA", rivitiedot[2])
            wpn.addAttribute("Con", rivitiedot[3])
            wpn.addAttribute("Avail", rivitiedot[4])
            wpn.addAttribute("Damage", rivitiedot[5])
            wpn.addAttribute("Ammo", rivitiedot[6])
            wpn.addAttribute("Shots", rivitiedot[7])
            wpn.addAttribute("ROF", rivitiedot[8])
            wpn.addAttribute("Rel", rivitiedot[9])
            wpn.addAttribute("Range", rivitiedot[10])
            wpn.addAttribute("Cost", rivitiedot[11])
            wpn.test_me()
            if wpn.fail:
                self.failure_wpns = self.failure_wpns +1
                self.failed_wpns.append(wpn.getAttribute('Name'))
                self.all_weapons[wpn.getAttribute('Name')] = wpn
            else:
                self.success_wpns = self.success_wpns +1
                target.append(wpn)
                self.all_weapons[wpn.getAttribute("Name")] = wpn
            wpn.count_avail_diff()
        d.close()
        #print(self.light_pistols[0].getAttributes())

    def read_armors(self, filepath, target):
        file = xml_file()
        file.load_file(filepath)
        root = file.root
        for node in root.iter('armor'):
            
            brand = str(node.find('brand').text)
            name = str(node.find('name').text)
            type = str(node.find('type').text)
            cost = str(node.find('cost').text)
            ev_num = int(node.find('ev').text)
            sp_elements = list(node.find('sp'))
            container = Armor(brand,name,cost,ev=ev_num)
            for sp_value in sp_elements:
                container.add_sp_location(sp_value.tag, sp_value.text)
            self.armors.append(container)
            #print(container)
            #print(self.armors)
    def get_armor(self, name):
        returned=0
        for armor in self.armors:
            if armor.get_attribute('full name')==name:
                returned = copy.deepcopy(armor)
        return returned

    def get_weapon(self, name):
        returned=0
        for key, weapon in self.all_weapons.items():
            if key==name:
                returned = copy.deepcopy(weapon)
        return returned
       
    def read_cyber(self, filepath):
        f = open(filepath, 'r')
        
        for line in f:
           merkkijono = line.strip()
           rivi = merkkijono.split("_", -1)
           if rivi[0]=='off':
               pass
           else:
               cyber = cyberitem(category=rivi[1], name=rivi[3], description_short=rivi[5], operation_diff=rivi[4], hum_loss=rivi[7], cost=rivi[6], req_item_type = rivi[2], starter='on')
               #print(rivi[3])
               self.cybers.append(cyber)
               
        f.close()
        
        #print(str(self.cybers))

    def load_cyber_descr_long(self):
        f = open('source/cyberware/long_descr.txt')
        
        for line in f:
            try:
                text = line.strip()
                array = text.split('_', -1)
                self.cyber_descr_long[array[0]]=array[1]
            except Exception:
                pass
        f.close()

    def set_cyber_descr_long(self):
        for key, value in self.cyber_descr_long.items():
            cyber = self.get_cyber(key)
            cyber.set_attribute('description_long', value)


    def get_cyber(self, name):
        returned = cyberitem()
        for cyber in self.cybers:
            if cyber.get_attribute('name')==name:
                returned = copy.deepcopy(cyber)
        return returned
      
    def get_stat_to_money(self, value):
        num = 1
        transfer = []
        transfer.append(0)
        transfer.append(num)

        for i in range(1, 30):
            transfer.append(transfer[i] * 2)

        d = random.randint(transfer[value-1], transfer[value])
        return d

    def make_preference_xml(self):
        x = xml_file()
        system = 'modified fuzion'
        x.create_root('preferences')
        x.create_sub_element('primary_stats', 'root')
        x.set_value('system',system,'primary_stats')
        primary_stats = []
        primary_desc = {}
        self.Read_file('source/attributes.txt', primary_stats)
        self.read_to_dictionary('source/descr_attries.txt',primary_desc, True,'_')

        for stat in primary_stats:
            text=str.lower(stat)
            x.create_sub_element('stat', 'primary_stats')
            x.set_value('name',text,'stat')
            x.set_text(primary_desc[stat],'stat')

        x.create_sub_element('secondary_stats','root')
        x.set_value('system',system,'secondary_stats')
        
        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','luck','stat')
        x.set_value('first_source','int','stat')
        x.set_value('second_source','ref','stat')
        x.set_value('multiplier','1','stat')
        x.set_value('divider','2','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','hum','stat')
        x.set_value('first_source','will','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','10,','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','rec','stat')
        x.set_value('first_source','str','stat')
        x.set_value('second_source','con','stat')
        x.set_value('multiplier','1','stat')
        x.set_value('divider','2','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','end','stat')
        x.set_value('first_source','con','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','2','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','run','stat')
        x.set_value('first_source','move','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','2','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','sprint','stat')
        x.set_value('first_source','move','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','3','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','swim','stat')
        x.set_value('first_source','move','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','1','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','leap','stat')
        x.set_value('first_source','move','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','1','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','hits','stat')
        x.set_value('first_source','body','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','5','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','stun','stat')
        x.set_value('first_source','body','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','5','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','sd','stat')
        x.set_value('first_source','con','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','2','stat')
        x.set_value('divider','1','stat')

        x.create_sub_element('stat','secondary_stats')
        x.set_value('name','res','stat')
        x.set_value('first_source','will','stat')
        x.set_value('second_source','none','stat')
        x.set_value('multiplier','3','stat')
        x.set_value('divider','1','stat')

        skills = []
        skill_categories = {}
        skill_desc = {}
        skill_stats = {}
        skill_chips ={}
        skill_diff = {}

        self.Read_file('source/skills.txt',skills)
        self.read_to_dictionary('source/skill_categories.txt',skill_categories, False)
        self.read_to_dictionary('source/skill_descriptions.txt',skill_desc)
        self.read_to_dictionary('source/attributes_skills.txt', skill_stats, False)
        self.read_to_dictionary('source/skills_chips.txt',skill_chips,True,'_')
        self.read_to_dictionary('source/skill_diff.txt',skill_diff,True,'_')


        x.create_sub_element('skills','root')
        x.set_value('system', system,'skills')
        for skill in skills:
            x.create_sub_element('skill', 'skills')
            x.create_sub_element('name','skill')
            x.set_text(skill,'name')

            x.create_sub_element('stat','skill')
            try:
                x.set_text(skill_stats[skill],'stat')
            except Exception:
                x.set_text('not found','stat')

            x.create_sub_element('category','skill')
            try:
                x.set_text(skill_categories[skill],'category')
            except Exception:
                x.set_text('not found','category')

            x.create_sub_element('description','skill')
            try:
                x.set_text(skill_desc[skill],'description')
            except Exception:
                x.set_text('not found','description')

            x.create_sub_element('chippable','skill')
            try:
                x.set_text(skill_chips[skill],'chippable')
            except Exception:
                x.set_text('not found','chippable')

            x.create_sub_element('diff_modifier','skill')
            try:
                x.set_text(skill_diff[skill],'diff_modifier')
            except Exception:
                x.set_text('not found','diff_modifier')

        x.create_sub_element('complications', 'root')
        x.set_value('system',system,'complications')
        complications = []
        complication_categories = {}
        complication_descriptions = {}

        self.Read_file('source/complications.txt', complications)
        self.read_to_dictionary('source/complication_categories.txt', complication_categories, False)
        self.read_to_dictionary('source/complications_descriptions.txt', complication_descriptions)

        for complication in complications:
            x.create_sub_element('complication', 'complications')
            x.create_sub_element('name', 'complication')
            x.set_text(complication, 'name')

            x.create_sub_element('category', 'complication')
            try:
                x.set_text(complication_categories[complication], 'category')
            except Exception:
                x.set_text('not found', 'category')

            x.create_sub_element('description', 'complication')
            try:
                x.set_text(complication_descriptions[complication],'description')
            except Exception:
                x.set_text('not found', 'description')

        
        x.create_sub_element('talents','root')
        x.set_value('system', system,'talents')

        talents = []
        talent_descriptions = {}

        self.Read_file('source/talents.txt',talents)
        self.read_to_dictionary('source/talent_descriptions.txt',talent_descriptions, separator='_')

        for talent in talents:
            x.create_sub_element('talent','talents')
            x.create_sub_element('name', 'talent')
            x.set_text(talent,'name')
            x.create_sub_element('description','talent')
            
            try:
                x.set_text(talent_descriptions[talent],'description')
            except Exception:
                x.set_text('not found', 'description')

        x.create_sub_element('perks', 'root')
        x.set_value('system', system, 'perks')
        perks = []
        perk_descriptions = {}

        self.Read_file('source/perks.txt',perks)
        self.read_to_dictionary('source/perk_descriptions.txt', perk_descriptions, separator='_')

        for perk in perks:
            x.create_sub_element('perk','perks')
            x.create_sub_element('name', 'perk')
            x.set_text(perk, 'name')
            
            x.create_sub_element('description', 'perk')

            try:
                x.set_text(perk_descriptions[perk], 'description')
            except Exception:
                x.set_text('not found', 'description')


        x.save_file('preferences.xml')