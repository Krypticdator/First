from Fuzion import Fuzion
from dice import Dice
from Task import Task
from xml_file import xml_file
from random import choice

class Character:
   
    def __init__(self):
        self.__attributes = {}
        self.__actions = {}
        self.__skills = {}
        self.__perks = {}
        self.__talents = {}
        self.__complications = {}
        self.__skill_dependencies = {}
        self.__fuzion = Fuzion()
        self.__dice = Dice()
        self.__items = []
        self.__likes = {}                           #First impression is throwed against other persons Pre + dice
        
                                                    #margin of success = thats how much they like you
                                                    #After first impression, person can try to throw against Pre + social skill + margin of failure - 
                                                    #margin of success + roll to improve rating

        self.all_abilities = {}
        self.all_abilities['skills'] = self.__skills
        self.all_abilities['perks'] = self.__perks
        self.all_abilities['talents'] = self.__talents
        self.all_abilities['complications'] = self.__complications

        self.__money = self.__dice.Roll()
        self.__name = "John Doe"
        
        f = open('source/attributes.txt', 'r')
        for line in f:
            self.__attributes[line[:-1]] = 5
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
        

    def InitNeeds(self):
        self.set_attribute("Tiredness", 0) #Increases every hour by 1 point, after 12 hours awake char will become affected by tiredness
                                           #And must throw int + roll against tiredness value to stay awake. sleeping will give 1/2 rec
                                           #back every two sleepinging hours
        self.set_attribute("Hunger", 0 )   #Will increase by 1/2 of body attribute per hour. eating will give 1/2 of rec + mods in food
                                           #After 24 points is reached, must roll con + dice against hungry value to avoid losing stun, then hits
        self.set_attribute("Fun", 0)

    def run_hour(self):
        self.set_attribute("Tiredness", self.get_attribute("Tiredness")+1)
        self.set_attribute("Hunger", self.get_attribute("Hunger")+1)
        self.set_attribute("Fun", self.get_attribute("Fun")+1)
    
    
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
        basepoints = self.__attributes[attribute] + self.__skills[skill]
        return basepoints

    def get_ability_list(self,name):
        return self.all_abilities[name]

    def set_to_ability_list(self, name, ability, value):
        dictionary = self.all_abilities[name]
        dictionary[ability] = value

    def get_skill_throw(self, skill):
        dice = self.__fuzion.Roll()
        try:
            skill_throw = dice + self.getBasepoints(skill)
            return skill_throw
        except Exception:
            return dice

        

    def getAttributeRoll(self, attribute):
        dice = self.__fuzion.Roll()
        attri = self.__attributes[attribute]
        skill_throw = dice + attri

        return skill_throw
   
    def getName(self):
        return self.__name
    
    def setRandomStats(self):
        for statsi in self.__attributes:
            dice = self.__dice.Roll(2, 5)
            self.__attributes[statsi] = dice
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
    
    def get_attributes(self):
        return  self.__attributes
   
    def set_attribute(self, attribute, value):
        self.__attributes[attribute] = int(value)
        self.calc_derived_stats()

    def get_attribute(self, attribute):
        try:
            return self.__attributes[attribute]
        except Exception:
            return 0

    def setLike(self, target, value):
        try:
            self.__likes[target].append(value)
            print("set like onnistui")
        except Exception:
            print("virhe set like funktiossa")
            self.__likes[target] = []
            self.__likes[target].append(value)
        

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
        luck = (self.__attributes["Int"] + self.__attributes["Ref"]) / 2
        hum = self.__attributes["Will"] * 10
        rec = (self.__attributes["Str"] + self.__attributes["Con"]) / 2
        end = self.__attributes["Con"] * 2
        run = self.__attributes["Move"] * 2
        sprint = self.__attributes["Move"] * 3
        swim = self.__attributes["Move"]
        leap = self.__attributes["Move"]
        hits = self.__attributes["Body"] * 5
        stun = self.__attributes["Body"] * 5
        sd   = self.__attributes["Con"] * 2
        res  = self.__attributes["Will"] * 3

        self.__attributes["Luck"] = luck
        self.__attributes["Hum"] = hum
        self.__attributes["Rec"] = rec
        self.__attributes["End"] = end
        self.__attributes["Run"] = run
        self.__attributes["Sprint"] = sprint
        self.__attributes["Swim"] = swim
        self.__attributes["Leap"] = leap
        self.__attributes["Hits"] = hits
        self.__attributes["Stun"] = stun
        self.__attributes["SD"] = sd
        self.__attributes["Res"] = res
        
        #print(self.__attributes)
    def giveRandomName(self, gender):
        firstnames = []
        lastnames = []
        f_nick_name = []
        l_nick_name = []
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
            self.__attributes["Full name"] = first_name + " " + second_name + " " + first_nick + " " + last_nick + " " + last_name
            print(self.__attributes["Full name"])
        except Exception:
            pass


    def save(self):
        x = xml_file()
        x.create_root("Character")
        x.create_sub_element("skills", "root")
        x.create_sub_element("attributes", "root")
        for attribute, value in self.__attributes.items():
            x.create_sub_element("attribute", "attributes")
            x.set_value("type", attribute, "attribute")
            x.set_text(str(value), "attribute")
        for skill, value in self.__skills.items():
            x.create_sub_element("skill", "skills")
            x.set_value("type", skill, "skill")
            x.set_text(str(value), "skill")
        x.save_file()