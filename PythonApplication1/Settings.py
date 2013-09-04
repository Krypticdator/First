from Weapon import Weapon
import random
class Settings(object):
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
            wpn.count_avail_diff()
            wpn.test_me()
            if wpn.fail:
                self.failure_wpns = self.failure_wpns +1
                self.failed_wpns.append(wpn.getAttribute('Name'))
                self.all_weapons[wpn.getAttribute('Name')] = wpn
            else:
                self.success_wpns = self.success_wpns +1
                target.append(wpn)
                self.all_weapons[wpn.getAttribute("Name")] = wpn
        d.close()
        #print(self.light_pistols[0].getAttributes())
      
    def get_stat_to_money(self, value):
        num = 1
        transfer = []
        transfer.append(0)
        transfer.append(num)

        for i in range(1, 30):
            transfer.append(transfer[i] * 2)

        d = random.randint(transfer[value-1], transfer[value])
        return d
