from dice import Dice
from random import choice
from Tools import File_control
class Year(object):
    def __init__(self):
        self.attributes = {}
        self.attributes['type'] = 'undefined'
class Lifepath(object):
    """description of class"""
    def __init__(self):
        self.event_menu = []
        self.a4_menu = []
        self.b4_menu = []
        self.disaster_menu = []
        self.lucky_menu = []
        self.disaster_do_menu = []
        self.friend_menu = []
        self.enemy_who_menu = []
        self.enemy_cause_menu = []
        self.enemy_hate_menu = []
        self.enemy_do_menu = []
        self.enemy_resources_menu = []
        self.love_menu = []
        self.love_complicated_menu = []
        self.love_mutual_menu = []
        self.love_problems_menu = []
        self.love_tragic_menu = []

        self.lifepath = []
        self.lifepath_years = []
        self.statistics = {}

        self.statistics["Luck 0"] = 0
        self.statistics["Luck 1"] = 0
        self.statistics["Luck 2"] = 0
        self.statistics["Luck 3"] = 0
        self.statistics["Luck 4"] = 0
        self.statistics["Luck 5"] = 0
        self.statistics["Luck 6"] = 0
        self.statistics["Luck 7"] = 0

        self.Read_file('lifepath/lp_event_menu.txt', self.event_menu)
        self.Read_file('lifepath/lp_4A_menu.txt', self.a4_menu)
        self.Read_file('lifepath/lp_4B_menu.txt', self.b4_menu)
        self.Read_file('lifepath/lp_disaster_strikes.txt', self.disaster_menu)
        self.Read_file('lifepath/lp_lucky.txt', self.lucky_menu)
        self.Read_file('lifepath/lp_disaster_do_something.txt', self.disaster_do_menu)
        self.Read_file('lifepath/lp_friend_relationship.txt', self.friend_menu)
        self.Read_file('lifepath/lp_enemy_who.txt', self.enemy_who_menu)
        self.Read_file('lifepath/lp_enemy_cause.txt', self.enemy_cause_menu)
        self.Read_file('lifepath/lp_enemy_hate.txt', self.enemy_hate_menu)
        self.Read_file('lifepath/lp_enemy_do.txt', self.enemy_do_menu)
        self.Read_file('lifepath/lp_enemy_resource.txt', self.enemy_resources_menu)
        self.Read_file('lifepath/lp_love_event.txt', self.love_menu)
        self.Read_file('lifepath/lp_love_complicated.txt', self.love_complicated_menu)
        self.Read_file('lifepath/lp_love_mutual.txt', self.love_mutual_menu)
        self.Read_file('lifepath/lp_love_problems.txt', self.love_problems_menu)
        self.Read_file('lifepath/lp_love_tragic.txt', self.love_tragic_menu)

    def init_lifepath(self, age):
        for i in range(0, age+1):
            empty = []
            self.lifepath.append(empty)

    def Read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

    def add_random_event(self, year=0):
        lifepath = []
        y = Year()
        event=choice(self.event_menu)
        y.attributes['type']=event
        lifepath.append(event)
        if self.event_menu[0] in lifepath:  #Big wins, big problems
            lifepath.append(choice(self.a4_menu))
            if self.a4_menu[0] in lifepath: #You get lucky
                y.attributes['type'] = 'lucky'
                lifepath.append(choice(self.lucky_menu))
                self.lucky(lifepath, y)
            else:                           #Disaster strikes
                y.attributes['type'] = 'disaster'
                lifepath.append(choice(self.disaster_menu))
                self.disaster(lifepath, y)
        if self.event_menu[1] in lifepath:  #Friends & Enemies
            lifepath.append(choice(self.b4_menu))
            if self.b4_menu[0] in lifepath: #Made a friend
                friend = choice(self.friend_menu)
                lifepath.append(friend)
                y.attributes['type'] = 'friend'
                y.attributes['friend type'] = friend

            else:                           #Made an enemy
                enemy_type = choice(self.enemy_who_menu)
                enemy_cause = choice(self.enemy_cause_menu)
                enemy_relation = choice(self.enemy_hate_menu)
                enemy_action = choice(self.enemy_do_menu)
                enemy_resources = choice(self.enemy_resources_menu)
                lifepath.append(enemy_type)
                lifepath.append(enemy_cause)
                lifepath.append(enemy_relation)
                lifepath.append(enemy_action)
                lifepath.append(enemy_resources)
                y.attributes['type']='enemy'
                y.attributes['enemy type']=enemy_type
                y.attributes['enemy cause'] = enemy_cause
                y.attributes['enemy relation'] = enemy_relation
                y.attributes['enemy action'] = enemy_action
                y.attributes['enemy resources'] =enemy_resources
        if self.event_menu[2] in lifepath: #Romance
            romance = choice(self.love_menu)
            lifepath.append(romance)
            y.attributes['type']='love'
            if self.love_menu[0] in lifepath:
                y.attributes['love type']='happy'
            if self.love_menu[1] in lifepath: #Tragic
                tragic = choice(self.love_tragic_menu)
                feeling = choice(self.love_mutual_menu)
                lifepath.append(tragic)
                lifepath.append(feeling)
                y.attributes['love type']='tragic love'
                y.attributes['mutual feelings'] = feeling
                y.attributes['tragedy'] = tragic
            if self.love_menu[2] in lifepath: #With problems
                problem = choice(self.love_problems_menu)
                lifepath.append(problem)
                y.attributes['love type'] = 'with problems'
                y.attributes['problem'] = problem
            if self.love_menu[3] in lifepath:
                y.attributes['love type'] = 'hot dates'
            if self.love_menu[4] in lifepath: #Complicated
                complication = choice(self.love_complicated_menu)
                lifepath.append(complication)
                y.attributes['love type'] = 'complicated'
                y.attributes['complication'] = complication

        lifepath.insert(0, len(self.lifepath[year]))
        self.lifepath[year].append(lifepath)
        y.attributes['year'] = year
        self.lifepath_years.append(y)
        #print(self.lifepath[year])
        #print(self.lifepath)
    
    def disaster(self, lifepath, year=Year()):
        if self.disaster_menu[0] in lifepath: #Financial lost or debt
            d = Dice()
            money = d.Roll(1, 10) * 100
            temp = money * -1
            year.attributes['money'] = str(temp)
            year.attributes['disaster type']='debt'
            lifepath.append("You have lost " + str(money) + " in Night City Dollars. If you cant pay this now, you have a debt to pay, in cash-or blood.")
        if self.disaster_menu[1] in lifepath: #imprisoment
            d = Dice()
            r = d.Roll(1, 10)
            lifepath.append("You have been in prison, or possibly held hostage (your choice) for " + str(r) + " months")
            year.attributes['disaster type'] = 'prison/hostage'
            year.attributes['prison time'] = str(r)
        if self.disaster_menu[2] in lifepath: #Illness or addiction
            lifepath.append("You have contracted either an illness or drug habit in this time. Lost 1 pt of REF permanently as a result.")
            year.attributes['disaster type'] = 'drugs/illness'
            year.attributes['effect'] = '-1 ref'
        if self.disaster_menu[3] in lifepath: #Betrayel
            lifepath.append("You have been backstabbed in some manner.")
            how = []
            how.append("you are being blackmailed.")
            how.append("your secret was exposed")
            how.append("you were betrayed by a close friend in either romance or career (you choose).")
            final = choice(how)
            lifepath.append(final)
            year.attributes['disaster type'] = 'betrayel'
            year.attributes['blackmail type'] = final
        if self.disaster_menu[4] in lifepath: #Accident
            lifepath.append("You were in some kind of terrible accident.")
            d = Dice()
            r = d.Roll(1, 10)
            what = []
            what.append("you were terribly maimed and must subtract -2 from your DEX.")
            what.append("you were hospitalized for " + str(r) + " months that year.")
            what.append("you have lost " + str(r) + " months of memory of that year.")
            what.append("you constantly relive nightmares of the accident and wake up screaming.")
            type  = choice(what)
            lifepath.append(type)
            year.attributes['disaster type'] = 'accident'
            year.attributes['accident type'] = type

        if self.disaster_menu[5] in lifepath: #Lover, friend or relative killed
            lifepath.append("You lost someone you really cared about.")
            how = []
            how.append("They died accidentally.")
            how.append("They were murdered by unknown parties.")
            how.append("They were murdered and you know who did it. You just need the proof.")
            type = choice(how)
            lifepath.append(type)
            year.attributes['disaster type'] = 'death'
            year.attributes['death type'] = type 
        if self.disaster_menu[6] in lifepath: #False accusation
            lifepath.append("You were set up.")
            what = []
            what.append("The accusation is theft")
            what.append("The accusation is cowardice")
            what.append("The accusation is murder")
            what.append("The accusation is rape")
            what.append("The accusation is lying or betrayel")
            accusation = choice(what)
            lifepath.append(accusation)
            year.attributes['disaster type'] = 'false accusation'
            year.attributes['accusation'] = accusation
        if self.disaster_menu[7] in lifepath: #Hunted by the Law
            lifepath.append("You are hunted by the law for crimes you may or may not have committed (your choice).")
            who = []
            who.append("Only a couple local renta-cops want you")
            who.append("It's an entire local Security force")
            who.append("It's an Altcult Militia")
            who.append("It's the FBI or equivalent national police force")
            official = choice(who)
            lifepath.append(official)
            year.attributes['disaster type'] = 'crime'
            year.attributes['hunter'] = official
        if self.disaster_menu[8] in lifepath: #Hunted by a Neo-Corp
            lifepath.append("You have angered some Corporate honcho")
            who = []
            who.append("It's a small, local firm")
            who.append("It's a larger corp with offices Citywide")
            who.append("It's a big, national corp with agents in most major cities")
            who.append("It's a huge multinational megacorp with armies, ninja and spies everywhere")
            corporation = choice(who)
            lifepath.append(corporation)
            year.attributes['disaster type'] = 'corporation'
            year.attributes['corporation type'] = corporation
        if self.disaster_menu[9] in lifepath: 
            lifepath.append("You have experienced some type of mental or physical breakdown")
            what = []
            what.append("It is some type of nervous disorder, probably from a bioplague- lose 1 pt. REF")
            what.append("It is some kind of mental problem; you suffer anxiety attacks and phobias. Lose 1 pt from your PRE Stat")
            what.append("It is a major psychosis. You hear voices, are violent, irrational, depressive. Lose 1 pt from your PRE, 1 from REF")
            complication = choice(what)
            lifepath.append(complication)
            year.attributes['disaster type'] = 'breakdown'
            year.attributes['breakdown type']= complication

    def lucky(self, lifepath, year=Year()):
        if self.lucky_menu[0] in lifepath: #Make a Powerful Connection in Local Government
            where = []
            where.append("It's in a local Security Force.")
            where.append("It's in a local Altcult Leader's Office.")
            where.append("It's in the City Mgr's Office.")
            connection = choice(where)
            lifepath.append(connection)
            year.attributes['lucky type']='powerful connection'
            year.attributes['connection type']=connection
            #self.statistics["Luck 0"] += 1

        elif self.lucky_menu[1] in lifepath or self.lucky_menu[2] in lifepath: #financial windfall or big score
            dice = Dice()
            money = dice.Roll(1, 10) * 100
            lifepath.append("You got " + str(money) + " dcd")
            year.attributes['lucky type']='fortune'
            year.attributes['amount'] = str(money)
            #self.statistics["Luck 1"] += 1

        elif self.lucky_menu[3] in lifepath: #Find a Sensei 
            lifepath.append("Begin at +2 or add +1 to a Martial Arts Skill of your choice.")
            year.attributes['lucky type']='sensei'
            #self.statistics["Luck 2"] += 1

        elif self.lucky_menu[4] in lifepath: #Find a Teacher
            lifepath.append("Add +1 to any INT based skill, or begin a new INT based skill at +2.")
            year.attributes['lucky type'] = 'teacher'
            #self.statistics["Luck 3"] += 1

        elif self.lucky_menu[6] in lifepath: #Local nomadpack
            lifepath.append("You can call upon them for one favor a month, equivalent to a Family Perk of +2.")
            year.attributes['lucky type'] = 'nomads'
            #self.statistics["Luck 4"] += 1

        elif self.lucky_menu[7] in lifepath: #local altcult friend
            lifepath.append("You may use him for inside information at a level of +2 Streetwise on any situation relating to that Altcult.")
            year.attributes['lucky type'] = 'altcult contact'

            #self.statistics["Luck 5"] += 1
        elif self.lucky_menu[8] in lifepath: #boostergang
            lifepath.append("Who knows why. These are Boosters, right? You can call upon them for 1 favor a month, equivalent to a Family Perk of +2. But dont push your luck..")
            year.attributes['lucky type'] = 'boostergang'
            self.statistics["Luck 6"] += 1

        elif self.lucky_menu[9] in lifepath: #combat teacher
            lifepath.append("Add +1 to any weapon skill with the exception of Martial Arts or Brawling, or begin a new combat skill at +2 .") 
            year.attributes['lucky type'] = 'combat teacher'             
            self.statistics["Luck 7"] += 1
        else:
            year.attributes['lucky type']='';
            print('lifepath includes ' + str(lifepath))

class Family(File_control):
    def __init__(self):
        self.early_backround_menu = []
        self.siblings_menu = []
        self.parents_menu = []
        self.parent_status_menu = []
        self.parent_event_menu = []
        self.family_status_menu = []
        self.family_event_menu = []
        self.childhood_enviroment_menu = []
        self.family_contact_menu = []
        self.childhood_trauma = []

        self.Read_file('lifepath/family/family_rank.txt', self.early_backround_menu)
        self.Read_file('lifepath/family/family_siblings.txt', self.siblings_menu)
        self.Read_file('lifepath/family/family_is.txt', self.parents_menu)
        self.Read_file('lifepath/family/family_is_2.txt', self.parent_status_menu)
        self.Read_file('lifepath/family/family_something_happened.txt', self.parent_event_menu)
        self.Read_file('lifepath/family/family_status.txt', self.family_status_menu)
        self.Read_file('lifepath/family/family_tragedy.txt', self.family_event_menu)
        self.Read_file('lifepath/family/childhood_enviroment.txt', self.childhood_enviroment_menu)
        self.Read_file('lifepath/family/family_contact.txt', self.family_contact_menu)
        self.Read_file('lifepath/family/childhood_trauma.txt', self.childhood_trauma)
        self.family_path = []
        self.family = {}

    def generate_family(self):
        self.family['rank']=choice(self.early_backround_menu)
        self.family['parents']=choice(self.parents_menu)
        parent_status = choice(self.parent_status_menu)
        if parent_status==self.parent_status_menu[1]:
            self.family['parent status'] = parent_status
            self.family['parent event'] = choice(self.parent_event_menu) 
        else:
            self.family['parent status'] = parent_status
        x = Dice()
        roll = x.Roll(1, 10)
        if roll >4:
            self.family['siblings'] = 'none'
        else:
            self.family['siblings'] = roll

        family_status = choice(self.family_status_menu)
        if family_status == self.family_status_menu[0]:
            self.family['family status'] = family_status
            self.family['family event'] = choice(self.family_event_menu)
        else:
            self.family['family status'] = family_status

        childhood = choice(self.childhood_enviroment_menu)
        self.family['childhood'] = childhood

        self.family['childhood trauma'] = choice(self.childhood_trauma)







        


