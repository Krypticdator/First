from Character import Character
from Settings import Settings
from Fuzion import Fuzion


class Controller():
    """description of class"""
    def __init__(self):
        self.__char = Character()
        #self.__char.setRandomStats()
        self.settings = Settings()
        self.datasets = {}
        self.max_cpoints=60
        self.max_opoints=50
        self.money = 2500
        self.datasets['headers']=[]

    def save(self):

        prime_motivation = self.datasets['Prime Motivation: '].var.get()
        most_v_person = self.datasets['Most valued person: '].var.get()
        most_v_pos = self.datasets['Most valued posession: '].var.get()
        valued_people = self.datasets['How do you feel about most people: '].var.get()
        inmode = self.datasets['Inmode:'].var.get()
        exmode = self.datasets['Exmode:'].var.get()

        quirk_value_dictionary = self.datasets['Quirks'].stringvars
        disorder_value_dictionary = self.datasets['Disorders'].stringvars
        phobia_value_dictionary = self.datasets['Phobias'].stringvars
        hair_value_dictionary = self.datasets['Hair'].stringvars
        clothes_value_dictionary = self.datasets['Clothes'].stringvars
        affe_value_dictionary = self.datasets['Affections'].stringvars
        quirk_array = []
        disorder_array = []
        phobia_array = []
        hair_array = []
        clothes_array = []
        affe_array = []
        for key, value in quirk_value_dictionary.items():
             try:
                if value.get() != "off":
                    
                    quirk_array.append(value.get())
             except Exception:
                if value != "off":
                    quirk_array.append(value)

        for key, value in disorder_value_dictionary.items():
             try:
                if value.get() != "off":
                    
                    disorder_array.append(value.get())
             except Exception:
                if value != "off":
                    disorder_array.append(value)

        for key, value in phobia_value_dictionary.items():
             try:
                if value.get() != "off":
                    
                    phobia_array.append(value.get())
             except Exception:
                if value != "off":
                    phobia_array.append(value)
        
        for key, value in hair_value_dictionary.items():
             try:
                if value.get() != "off":
                    
                    hair_array.append(value.get())
             except Exception:
                if value != "off":
                    hair_array.append(value)

        
        for key, value in clothes_value_dictionary.items():
             try:
                if value.get() != "off":
                    
                    clothes_array.append(value.get())
             except Exception:
                if value != "off":
                    clothes_array.append(value)

        
        for key, value in affe_value_dictionary.items():
             try:
                if value.get() != "off":
                    
                    affe_array.append(value.get())
             except Exception:
                if value != "off":
                    affe_array.append(value)
        
        self.__char.set_attribute('player', self.datasets['player'].get())
        self.__char.set_attribute('First name', self.datasets['first name'].get())
        self.__char.set_attribute('Second name', self.datasets['second name'].get())
        self.__char.set_attribute('Last name', self.datasets['last name'].get())
        self.__char.set_attribute('Alias', self.datasets['alias'].get())
        self.__char.set_attribute('age', self.datasets['age'].get())

        self.__char.set_attribute('family rank', self.datasets['Family rank'].var.get())
        self.__char.set_attribute('parents', self.datasets['Your parents were'].var.get())
        self.__char.set_attribute('parent status', self.datasets['Parent status'].var.get())
        self.__char.set_attribute('parent event', self.datasets['Parent event'].var.get())
        self.__char.set_attribute('family status', self.datasets['Family status'].var.get())
        self.__char.set_attribute('family event', self.datasets['Family event'].var.get())
        self.__char.set_attribute('childhood enviroment', self.datasets['Childhood enviroment'].var.get())
        self.__char.set_attribute('childhood trauma/fortune', self.datasets['Childhood trauma/fortune'].var.get())
        self.__char.set_attribute('family contact', self.datasets['Family contact'].var.get())
        
        
        try:
            self.__char.set_siblings(self.datasets['siblings'])
        except Exception:
            pass
        

        self.__char.set_attribute('prime motivation', prime_motivation)
        self.__char.set_attribute('most valued person', most_v_person)
        self.__char.set_attribute('most valued posession', most_v_pos)
        self.__char.set_attribute('feels about people', valued_people)
        self.__char.set_attribute('inmode', inmode)
        self.__char.set_attribute('exmode', exmode)
        self.__char.set_attribute('quirks', quirk_array)
        self.__char.set_attribute('disorders', disorder_array)
        self.__char.set_attribute('phobias', phobia_array)
        self.__char.set_attribute('hair', hair_array)
        self.__char.set_attribute('clothes', clothes_array)
        self.__char.set_attribute('affections', affe_array)
        self.__char.set_lifepath(self.datasets['lifepath'])
        self.__char.save()

    def getChar_stats(self):
        return self.__char_get_attributes()

    def recalculate_points(self):
        statbox = self.datasets['stats']
        skills = self.get_ability_dictionary('skills')
        perks = self.get_ability_dictionary('perks')
        talents = self.get_ability_dictionary('talents')
        complications = self.get_ability_dictionary('complications')
        weapons = self.get_ability_dictionary('weapons')
        armors = self.get_ability_dictionary('armor')
        cpoint_sum = 0
        opoint_sum = 0

        for key, value in statbox.variables.items():
            cpoint_sum = cpoint_sum + int(value.get())

        for key, value in skills.items():
            try:
                if int(value)!=0:
                    opoint_sum = opoint_sum + int(value)
            except Exception:
                pass

        for key, value in perks.items():
            try:
                if key.count('Favor'):
                    cost = int(value) * 0.5
                    opoint_sum = opoint_sum + cost
                elif key.count('Wealth'):
                    cost = int(value) * 5
                    opoint_sum = opoint_sum + cost
                else:
                    opoint_sum = opoint_sum + int(value)
            except Exception:
                pass

        for key, value in talents.items():
            try:
                cost = int(value) * 3
                opoint_sum = opoint_sum + cost
            except Exception:
                pass

        comp_total_limit = self.max_opoints * 0.5
        comp_total_current = 0
        op_current_limit=self.max_opoints
        for key, value in complications.items():
            try:
                cost = float(value.attributes['total'])
                if cost + comp_total_current <=comp_total_limit:
                    comp_total_current = comp_total_current + cost
                    op_current_limit = op_current_limit + cost
                    #opoint_sum = opoint_sum - cost
                else:
                    op_current_limit = self.max_opoints + comp_total_limit
            except Exception:
                pass

        money_sum=0
        for key, value in weapons.items():
            try:
                money_sum=money_sum + int(value)
            except Exception:
                pass

        for key, value in armors.items():
            try:
                money_sum = money_sum +int(value)
            except Exception:
                pass

            


        cpoint_sum = self.max_cpoints - cpoint_sum
        opoint_sum = op_current_limit - opoint_sum
        money_sum = self.money - money_sum

        cpoint_text = str(cpoint_sum) + '/' + str(self.max_cpoints)
        opoint_text = str(opoint_sum) + '/' + str(op_current_limit)

        for header in self.datasets['headers']:
            header.var_cpoints.set(cpoint_text)
            header.var_opoints.set(opoint_text)
            header.var_money.set(str(money_sum))

        #self.var_cpoints.set(str(cpoint_text))
        #self.var_opoints.set(opoint_text)

    def get_Wpn_availability(self):
        return self.__char.getAttributeRoll("Luck")

    def getChar_stat(self, stat):
        return self.__char.get_stat(stat)

    def setChar_stat(self, stat, value):
        self.__char.set_stat(stat, value)

    def clear_all_skills(self):
        list = self.__char.get_skills()

        for key, value in list.items():
            list[key] = 0

    def set_char_skill(self, skill, value):
        self.__char.add_skill(skill, value)

    def get_char_skill_dictionary(self):
        return self.__char.get_skills()

    def clear_ability_list(self, name):
        list = self.__char.get_ability_list(name)

        if name!='cyberware':
            list.clear()
        else:
            del list[:]
            

    def set_to_ability_list(self, list, ability, value, complication=False, frequency=0, intensity=0, importance=0):
        self.__char.set_to_ability_list(list, ability, value, complication, frequency, intensity, importance)

    def get_from_ability_list(self, list, ability):
        ability = self.__char.get_ability(list, ability)
        return ability

    def get_ability_dictionary(self, list_name):
        list = self.__char.get_ability_list(list_name)
        return list

    def get_char_cyberwear(self):
        return self.__char.get_installed_cyberwear()

    def print_all_abilities(self):
        for key, dictionary in self.__char.all_abilities.items():
            for key2, value in dictionary.items():
                if value!=0:
                    print(key2 + ' ' + value)

    def get_char_skill(self, skill):
        return self.__char.get_skill(skill)

    def get_r_name(self, nametype, gender="undecided"):
        x = Character()
        x.giveRandomName(gender)

        if nametype == "first":
            self.__char.set_attribute('First name', x.get_attribute('First name'))
            return x.get_attribute("First name")
        if nametype == "second":
            self.__char.set_attribute('Second name', x.get_attribute('Second name'))
            return x.get_attribute("Second name")
        if nametype == "last":
            self.__char.set_attribute('Last name', x.get_attribute('Last name'))
            return x.get_attribute("Last name")
        if nametype == "nick":
            self.__char.set_attribute('First alias', x.get_attribute('First alias'))
            self.__char.set_attribute('Last alias', x.get_attribute('Last alias'))
            alias =x.get_attribute("First alias") +' '+ x.get_attribute("Last alias")
            self.__char.set_attribute('Alias',alias)
            return alias

    def set_char_attribute(self, name, attribute):
        self.__char.set_attribute(attribute, attribute)
    def set_char_comp(self, complication, intensity, frequency, importance, total):
        self.__char.set_complication(complication, intensity, frequency, importance, total)
