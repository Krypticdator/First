from Fuzion import Fuzion
from dice import Dice
from Task import Task
from xml_file import xml_file
from random import choice

class Character:
   
    def __init__(self):
        self.__attributes = {}
        self.__stats = {}
        self.__actions = {}
        self.__skills = {}
        self.__perks = {}
        self.__talents = {}
        self.__armors = {}
        self.__weapons={}
        self.__cyberwear = []
        self.__complications = {}
        self.__skill_dependencies = {}
        self.__fuzion = Fuzion()
        self.__dice = Dice()
        self.__items = {}
        self.__likes = {}                           #First impression is throwed against other persons Pre + dice
        
                                                    #margin of success = thats how much they like you
                                                    #After first impression, person can try to throw against Pre + social skill + margin of failure - 
                                                    #margin of success + roll to improve rating

        self.all_abilities = {}
        self.all_abilities['skills'] = self.__skills
        self.all_abilities['perks'] = self.__perks
        self.all_abilities['talents'] = self.__talents
        self.all_abilities['complications'] = self.__complications
        self.all_abilities['armor'] = self.__armors
        self.all_abilities['cyberwear'] = self.__cyberwear
        self.all_abilities['items'] = self.__items
        self.all_abilities['weapons'] = self.__weapons

        self.__money = self.__dice.Roll()
        self.__name = "John Doe"
        
        f = open('source/attributes.txt', 'r')
        for line in f:
            self.__stats[line[:-1]] = 50
        f.close()
        print("hi")

        e = open('source/skills.txt', 'r')
        for line in e:
            self.__skills[line[:-1]]  = 0
        e.close()

        d = open('source/attributes_skills.txt', 'r')
        for line in d:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.partition(";")
            self.__skill_dependencies[rivitiedot[2]] = rivitiedot[0]
        d.close()

        self.calc_derived_stats()
        self.InitNeeds()
        self.InitActions()
        print(self)

    def InitNeeds(self):
        self.set_stat("Tiredness", 0) #Increases every hour by 1 point, after 12 hours awake char will become affected by tiredness
                                           #And must throw int + roll against tiredness value to stay awake. sleeping will give 1/2 rec
                                           #back every two sleepinging hours
        self.set_stat("Hunger", 0 )   #Will increase by 1/2 of body attribute per hour. eating will give 1/2 of rec + mods in food
                                           #After 24 points is reached, must roll con + dice against hungry value to avoid losing stun, then hits
        self.set_stat("Fun", 0)

    def run_hour(self):
        self.set_stat("Tiredness", self.get_stat("Tiredness")+1)
        self.set_stat("Hunger", self.get_stat("Hunger")+1)
        self.set_stat("Fun", self.get_stat("Fun")+1)
    
    
    def Talk_to(self, target):
        try:
            self.__likes[target.getName()]
            
        except Exception:
            roll = self.getAttributeRoll("Pre")
            targetroll = target.get_attribute("Pre") + self.__fuzion.Roll()
            self.__fuzion.__
            self.__likes[target.getName()] = 0
            print("ei onnistunut")

    def InitActions(self):
        impression = Task()
        talk = Task()
        
        impression.set_c_attribute("Pre",self)

        self.__actions["Impression"] = impression
        self.__actions["Talk"] = talk
    
    def MakeImpression(self, target):
        try:
            target.getLike(self.__name)
        except Exception:
            print("virhe")
            t = self.__actions["Impression"]
            x = t.Q_attribute_race(self, target, "Pre", "Pre")
            target.setLike(self.__name, x)
    
    def Talk(self, target):
        try:
            t = self.__actions["Talk"]
            t.set_c_attribute("Pre", self)
            t.set_c_skill("Persuasion & Fast Talk", self)
            t.set_t_attribute("Pre", target)
            x = sum(target.getLike(self.__name)) / len(target.getLike(self.__name))
            print(x)
            if x < 0:
             x =   x / (-1)
            else:
             x =   x * (-1)

            print(x)
            t.set_t_skill("none", target, x)
            y = t.Run_Custom()
            target.setLike(self.__name, y)
        except Exception:
            self.MakeImpression(target)

    def Challenge(self, Target, c_skill, t_skill):
        t = Task()
        result = t.Q_race(self, Target, c_skill, t_skill)
        return result
   
    def Random_all(self):
        self.setRandomSkills()
        self.setRandomStats()

    def getBasepoints(self, skill):
        attribute = self.__skill_dependencies[skill]
        basepoints = self.__stats[attribute] + self.__skills[skill]
        return basepoints

    def get_ability_list(self,name):
        return self.all_abilities[name]

    def get_ability(self, listname, ability):
        if listname == 'cyberware':
            return 0
        else:
            dictionary = self.all_abilities[listname]
            return dictionary[ability]

    def get_installed_cyberwear(self):
        cyberwear_list = []
        for cyberwear in self.__cyberwear:
            if cyberwear.get_attribute('name')=='default':
                for option in cyberwear.get_attribute('installed_options'):
                    cyberwear_list.append(option)
            else:
                cyberwear_list.append(cyberwear)
                for option in cyberwear.get_attribute('installed_options'):
                    cyberwear_list.append(option)
        #print(str(len(cyberwear_list)))
        return cyberwear_list

    def set_to_ability_list(self, name, ability, value=0, complication=False, frequency=0, intensity=0, importance=0):
        try:
            dictionary = self.all_abilities[name]
        except Exception:
            self.all_abilities[name]=[]
            dictionary = self.all_abilities[name]
        if name=='cyberwear':
            try:
                dictionary.append(ability)
            except Exception:
                dictionary = []
        else:
            dictionary[ability] = value
        if complication:
            comp = Stat(name=ability)
            comp.attributes['frequency']=frequency
            comp.attributes['intensity']=intensity
            comp.attributes['importance']=importance
            comp.attributes['total'] = value
            dictionary[ability]=comp
            #print('complication adding success')

    def get_skill_throw(self, skill):
        dice = self.__fuzion.Roll()
        try:
            skill_throw = dice + self.getBasepoints(skill)
            return skill_throw
        except Exception:
            return dice

        

    def getAttributeRoll(self, attribute):
        dice = self.__fuzion.Roll()
        attri = self.__stats[attribute]
        skill_throw = dice + attri

        return skill_throw
   
    def getName(self):
        return self.__name
    
    def setRandomStats(self):
        for statsi in self.__stats:
            dice = self.__dice.Roll(2, 5)
            self.__stats[statsi] = dice
        #print(self.__attributes)
        self.calc_derived_stats()

    def setRandomSkills(self):
        for skill in self.__skills:
            dice = self.__dice.Roll(1, 10)
            self.__skills[skill] = dice
   
    def add_custom_skill(self, skillname, attribute, lvl=0):
        self.__skill_dependencies[skillname] = attribute
        self.__skills[skillname] = lvl

    def add_skill(self, skillname, lvl = 0):
        self.__skills[skillname] = lvl
    
    def get_stats(self):
        return  self.__stats
   
    def set_stat(self, attribute, value):
        self.__stats[attribute] = int(value)
        self.calc_derived_stats()

    def get_stat(self, attribute):
        try:
            return self.__stats[attribute]
        except Exception:
            return 0

    def get_attribute(self, attribute):
        return self.__attributes[attribute]
    def set_attribute(self, attribute, value):
        self.__attributes[attribute] = value
    def set_complication(self, complication, intensity, frequency, importance, total):
        stat = Stat(total, total, complication)
        stat.attributes['intensity']=intensity
        stat.attributes['frequency']=frequency
        stat.attributes['importance']=importance
        
    def setLike(self, target, value):
        try:
            self.__likes[target].append(value)
            print("set like onnistui")
        except Exception:
            print("virhe set like funktiossa")
            self.__likes[target] = []
            self.__likes[target].append(value)

    def set_siblings(self, array):
        self.siblings = array
        

    def getLike(self, target):
        return self.__likes[target]
    
    def get_skill(self, skill):
        if skill in self.__skills:
            return self.__skills[skill]
        else:
            self.__skills[skill] = 0
            return self.__skills[skill]
    def get_skills(self):
        return self.__skills

    def calc_derived_stats(self):
        luck = (self.__stats["Int"] + self.__stats["Ref"]) / 2
        hum = self.__stats["Will"] * 10
        rec = (self.__stats["Str"] + self.__stats["Con"]) / 2
        end = self.__stats["Con"] * 2
        run = self.__stats["Move"] * 2
        sprint = self.__stats["Move"] * 3
        swim = self.__stats["Move"]
        leap = self.__stats["Move"]
        hits = self.__stats["Body"] * 5
        stun = self.__stats["Body"] * 5
        sd   = self.__stats["Con"] * 2
        res  = self.__stats["Will"] * 3

        self.__stats["Luck"] = luck
        self.__stats["Hum"] = hum
        self.__stats["Rec"] = rec
        self.__stats["End"] = end
        self.__stats["Run"] = run
        self.__stats["Sprint"] = sprint
        self.__stats["Swim"] = swim
        self.__stats["Leap"] = leap
        self.__stats["Hits"] = hits
        self.__stats["Stun"] = stun
        self.__stats["SD"] = sd
        self.__stats["Res"] = res
        
        #print(self.__attributes)
    def giveRandomName(self, gender='undecided'):
        firstnames = []
        lastnames = []
        f_nick_name = []
        l_nick_name = []
        if gender=='undecided':
            gender_table = []
            gender_table.append('Male')
            gender_table.append('Female')
            gender = choice(gender_table)
        try:
            if gender == "Male":
                f = open('source/firstnames.txt', 'r')
                for line in f:
                    merkkijono = line.strip()
                    firstnames.append(merkkijono)
                f.close()
            if gender == "Female":
                f = open('source/female_names.txt', 'r')
                for line in f:
                    merkkijono = line.strip()
                    firstnames.append(merkkijono)
                f.close()

            f = open('source/lastnames.txt', 'r')
            for line in f:
                merkkijono = line.strip()
                lastnames.append(merkkijono)
            f.close()

            f = open('source/first_nick_name.txt', 'r')
            for line in f:
                merkkijono = line.strip()
                f_nick_name.append(merkkijono)
            f.close()

            f = open('source/last_nick_name.txt', 'r')
            for line in f:
                merkkijono = line.strip()
                l_nick_name.append(merkkijono)
            f.close()

            first_name = choice(firstnames)
            second_name = choice(firstnames)
            last_name = choice(lastnames)
            first_nick = choice(f_nick_name)
            last_nick = choice(l_nick_name)
            self.__attributes["First name"] = str.capitalize(first_name)
            self.__attributes["Second name"] = str.capitalize(second_name)
            self.__attributes["Last name"] = str.capitalize(last_name)
            self.__attributes["First alias"] = str.capitalize(first_nick)
            self.__attributes["Last alias"] = str.capitalize(last_nick)
            self.__attributes['Alias'] = first_nick + ' ' + last_nick
            self.__attributes["Full name"] = str.capitalize(first_name) + " " + str.capitalize(second_name) + " " + first_nick + " " + last_nick + " " + str.capitalize(last_name)
            #print(self.__attributes["Full name"])
        except Exception:
            pass

    def set_lifepath(self, lifepath):
        self.lifepath = lifepath

    

    def save(self):
        x = xml_file()
        x.create_root("Character")
        x.create_sub_element('info', 'root')
        x.create_sub_element('family', 'root')
        x.create_sub_element('personality','root')
        x.create_sub_element("skills", "root")
        x.create_sub_element("attributes", "root")
        x.create_sub_element('perks', 'root')
        x.create_sub_element('talents', 'root')
        
        x.create_sub_element('complications', 'root')
        x.create_sub_element('cyberwears', 'root')
        x.create_sub_element('items', 'root')
        x.create_sub_element('lifepath', 'root')

        x.create_sub_element('player', 'info')
        x.create_sub_element('first_name', 'info')
        x.create_sub_element('second_name', 'info')
        x.create_sub_element('last_name', 'info')
        x.create_sub_element('alias', 'info')
        x.create_sub_element('age', 'info')

        x.create_sub_element('family_rank', 'family')
        x.create_sub_element('parents', 'family')
        x.create_sub_element('parent_status', 'family')
        x.create_sub_element('parent_event', 'family')
        x.create_sub_element('family_status', 'family')
        x.create_sub_element('family_event', 'family')
        x.create_sub_element('childhood_enviroment', 'family')
        x.create_sub_element('childhood_trauma_fortune', 'family')
        x.create_sub_element('family_contact', 'family')
        x.create_sub_element('siblings', 'family')

        x.create_sub_element('prime_motivation', 'personality')
        x.create_sub_element('most_valued_person', 'personality')
        x.create_sub_element('most_valued_posession','personality')
        x.create_sub_element('feels_about_people','personality')
        x.create_sub_element('inmode','personality')
        x.create_sub_element('exmode','personality')
        
        x.set_text(self.get_attribute('player'), 'player')
        x.set_text(self.get_attribute('First name'), 'first_name')
        x.set_text(self.get_attribute('Second name'), 'second_name')
        x.set_text(self.get_attribute('Last name'), 'last_name')
        alias = self.get_attribute('Alias')
        x.set_text(alias, 'alias')
        x.set_text(str(self.get_attribute('age')),'age')

        x.set_text(self.get_attribute('family rank'), 'family_rank')
        x.set_text(self.get_attribute('parents'), 'parents')
        x.set_text(self.get_attribute('parent status'), 'parent_status')
        x.set_text(self.get_attribute('parent event'), 'parent_event')
        x.set_text(self.get_attribute('family status'), 'family_status')
        x.set_text(self.get_attribute('family event'), 'family_event')
        x.set_text(self.get_attribute('childhood enviroment'),'childhood_enviroment')
        x.set_text(self.get_attribute('childhood trauma/fortune'),'childhood_trauma_fortune')
        x.set_text(self.get_attribute('family contact'), 'family_contact')
        
        try:
            for sibling in self.siblings:
                x.create_sub_element('sibling', 'family')
                x.set_value('gender', sibling.gender, 'sibling')
                x.set_value('age', str(sibling.age), 'sibling')
                x.set_value('relation', sibling.relation, 'sibling')
                x.set_text(sibling.name, 'sibling')
        except Exception:
            x.create_sub_element('sibling', 'siblings')
            x.set_value('gender', 'none', 'sibling')
            x.set_value('age', '0', 'sibling')
            x.set_value('relation', 'none', 'sibling')
            x.set_text('you are the only child', 'sibling')

        x.set_text(self.get_attribute('prime motivation'), 'prime_motivation')
        x.set_text(self.get_attribute('most valued person'),'most_valued_person')
        x.set_text(self.get_attribute('most valued posession'),'most_valued_posession')
        x.set_text(self.get_attribute('feels about people'),'feels_about_people')
        x.set_text(self.get_attribute('inmode'),'inmode')
        x.set_text(self.get_attribute('exmode'),'exmode')

        for quirk in self.get_attribute('quirks'):
            x.create_sub_element('quirk', 'personality')
            x.set_text(quirk, 'quirk')

        for disorder in self.get_attribute('disorders'):
            x.create_sub_element('disorder', 'personality')
            x.set_text(disorder, 'disorder')

        for phobia in self.get_attribute('phobias'):
            x.create_sub_element('phobia', 'personality')
            x.set_text(phobia, 'phobia')

        for hair in self.get_attribute('hair'):
            x.create_sub_element('hair', 'personality')
            x.set_text(hair, 'hair')

        for clothes in self.get_attribute('clothes'):
            x.create_sub_element('clothes', 'personality')
            x.set_text(clothes, 'clothes')

        for affe in self.get_attribute('affections'):
            x.create_sub_element('affection', 'personality')
            x.set_text(affe, 'affection')


        for attribute, value in self.__stats.items():
            x.create_sub_element("attribute", "attributes")
            x.set_value("type", attribute, "attribute")
            x.set_text(str(value), "attribute")
        for skill, value in self.__skills.items():
            x.create_sub_element("skill", "skills")
            x.set_value("type", skill, "skill")
            x.set_text(str(value), "skill")
        for perk, value in self.__perks.items():
            x.create_sub_element("perk", "perks")
            x.set_value("type", perk, "perk")
            x.set_text(str(value), "perk")
        for talent, value in self.__talents.items():
            x.create_sub_element('talent', 'talents')
            x.set_value('type', talent, 'talent')
            x.set_text(str(value), 'talent')

        for complication, value in self.__complications.items():
            try:
                x.create_sub_element("complication", "complications")
                x.set_value("type", str(value), "complication")
                x.set_value('intensity', value.attributes['intensity'], 'complication')
                x.set_value('frequency', value.attributes['frequency'], 'complication')
                x.set_value('importance', value.attributes['importance'], 'complication')
                x.set_text(str(value.attributes['total']), 'complication')
                #x.set_text(str(value), "complication")
            except Exception:
                print('failed to include complication into save file')
        
        
        try:
            for cyberwear in self.__cyberwear:
                if cyberwear.get_attribute('name')=='default':
                    for option in cyberwear.get_attribute('installed_options'):
                        x.create_sub_element('cyberwear', 'cyberwears')
                        x.set_value('name', option.get_attribute('name'), 'cyberwear')
                        x.set_text(str(option.get_attribute('effective_hum_cost')),'cyberwear')
                else:
                    x.create_sub_element('cyberwear', 'cyberwears')
                    x.set_value('name', cyberwear.get_attribute('name'), 'cyberwear')
                    x.set_text(cyberwear.get_attribute('effective_hum_cost'),'cyberwear')
                    for option in cyberwear.get_attribute('installed_options'):
                        x.create_sub_element('option', 'cyberwear')
                        x.set_value('name', option.get_attribute('name'), 'option')
                        x.set_text(option.get_attribute('effective_hum_cost'), 'option')
        except Exception:
            print('failed to save cyberware')

        for key, value in self.__weapons.items():
            x.create_sub_element('item', 'items')
            x.set_value('type', 'weapon', 'item')
            x.set_text(key, 'item')

        for key, value in self.__armors.items():
            x.create_sub_element('item', 'items')
            x.set_value('type', 'armor', 'item')
            x.set_text(key, 'item')

        for key, value in self.__items.items():
            x.create_sub_element('item', 'items')
            x.set_value('type','item','item')
            x.set_text(key, 'item')

        for year in self.lifepath:
            x.create_sub_element('event', 'lifepath')
            x.set_value('age',year.attributes['year'], 'event')
            type = year.attributes['type']
            x.set_value('type', type, 'event')
            if type=='disaster':
                disaster = year.attributes['disaster type']
                x.set_value('disaster_type', disaster, 'event')
                if disaster == 'debt':
                    x.set_value('amount', year.attributes['money'], 'event')
                elif disaster == 'prison/hostage':
                    x.set_value('prison_time',year.attributes['prison time'], 'event')
                elif disaster =='drugs/illness':
                    x.set_value('effect', year.attributes['effect'], 'event')
                elif disaster =='betrayel':
                    x.set_value('betrayel_type', year.attributes['blackmail type'], 'event')
                elif disaster =='accident':
                    x.set_value('accident_type', year.attributes['accident type'], 'event')
                elif disaster =='death':
                    x.set_value('death_type', year.attributes['death type'], 'event')
                elif disaster =='false accusation':
                    x.set_value('accusation', year.attributes['accusation'], 'event')
                elif disaster == 'crime':
                    x.set_value('hunter', year.attributes['hunter'], 'event')
                elif disaster == 'corporation':
                    x.set_value('corporation_type', year.attributes['corporation type'], 'event')
                elif disaster =='breakdown':
                    x.set_value('complication', year.attributes['breakdown type'], 'event')
            elif type=='lucky':
                lucky = year.attributes['lucky type']
                x.set_value('lucky_type', lucky, 'event')
                if lucky == 'powerful connection':
                    x.set_value('connection_type', year.attributes['connection type'],'event')
                elif lucky == 'fortune':
                    x.set_value('amount',year.attributes['amount'], 'event')
                else:
                    pass
            elif type=='friend':
                friend = year.attributes['friend type']
                x.set_value('friend_type', friend, 'event')
            elif type=='enemy':
                enemy_type = year.attributes['enemy type']
                enemy_cause= year.attributes['enemy cause']
                enemy_relation = year.attributes['enemy relation']
                enemy_action = year.attributes['enemy action']
                enemy_resources = year.attributes['enemy resources']
                x.set_value('enemy_type', enemy_type, 'event')
                x.set_value('cause', enemy_cause, 'event')
                x.set_value('relation', enemy_relation, 'event')
                x.set_value('reaction', enemy_action, 'event')
                x.set_value('resources', enemy_resources, 'event') 
            elif type=='love':
                love_type = year.attributes['love type']
                x.set_value('love_type', love_type, 'event')
                if love_type=='tragic love':
                    x.set_value('mutual_feelings', year.attributes['mutual feelings'], 'event')
                    x.set_value('tragic_type', year.attributes['tragedy'], 'event')
                elif love_type=='with problems':
                    x.set_value('problem', year.attributes['problem'], 'event')
                elif love_type=='complicated':
                    x.set_value('complication', year.attributes['complication'], 'event')

        player = self.get_attribute('player') 
        full_name = self.get_attribute('First name') + ' ' +self.get_attribute('Second name') + ' ' + self.get_attribute('Alias') + ' ' +self.get_attribute('Last name') 
        if player != 'npc':
            x.save_file('playerchars/' + player + '_' +full_name)
        else:
            x.save_file('npcs/' + full_name)
        x.save_file("lastchar_saved.xml")

class Stat(object):
    def __init__(self, current=0, original=0, name='stat'):
        self.current=current
        self.original=original
        self.name=name
        self.attributes ={}
    def __str__(self):
        return self.name