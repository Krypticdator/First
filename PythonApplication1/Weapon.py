class Weapon(object):
    """description of class"""

    def __init__(self):
        self.__attributes = {}

        self.__attributes["Name"] = "" 
        self.__attributes["Type"] = ""
        self.__attributes["WA"] = "" 
        self.__attributes["Con"] = "" 
        self.__attributes["Avail"] = "" 
        self.__attributes["Damage"] = ""
        self.__attributes["Ammo"] = "" 
        self.__attributes["BodMin"] = "" 
        self.__attributes["Shots"] = "" 
        self.__attributes["ROF"] = "" 
        self.__attributes["Rel"] = "" 
        self.__attributes["Range"] = "" 
        self.__attributes["Cost"] = "" 
        self.__attributes["Source"] = ""
        self.__attributes["Avail_diff"] = ""

    def test_type(self):
        type = self.__attributes["Type"]
        typetext = "fail"
        if type == "P":
            typetext = 'Pistol'
        elif type == "SMG":
            typetext = 'Submachinegun'
        elif type == "SHT":
            typetext = 'Shotgun'
        elif type == "RIF":
            typetext = 'Rifle'
        elif type == "HVY":
            typetext = "Heavy"
        else:
            typetext = 'fail'
            self.fail = True

        self.__attributes["type_text"] = typetext

    def test_ava(self):
        ava = self.__attributes["Avail"]
        avatext = 'fail'
        if ava == 'E':
            avatext = 'Excellent'
            #print(avatext) 
        elif ava == 'C':
            diff = 18
            avatext = 'Common'
            #print(avatext) 
        elif ava == 'P':
            avatext = 'Poor'
            #print(avatext) 
        elif ava == 'R':
            avatext = 'Rare'
            #print(avatext) 
        elif ava == 'N':
            avatext = 'Unavailable'
            #print(avatext) 
        else:
            #print('in else statement of test_me') 
            #avatext = 'fail'
            self.fail = True
        self.__attributes["ava_text"] = avatext

    def test_con(self):
        context = 'fail'
        con = self.__attributes['Con']
        if con =='P':
            context = 'Pocket, Pants or Sleeve'
        elif con == 'J':
            context = 'Jacket, Coat or Shoulder Rig'
        elif con == 'L':
            context = 'Long Coat'
        elif con == 'N':
            context = 'Cant be Hidden'
        else:
            #con = 'fail'
            self.fail = True
        self.__attributes["con_text"] = context

    def test_WA(self):
        wa = self.__attributes["WA"]
        try:
            wa_int = int(wa)
        except Exception:
            self.fail = True

    def test_dmg(self):
        dmg = self.__attributes['Damage']
        dmg_dices=0
        dmg_sides=0
        bonus_dmg=0
        #print(len(dmg))
        #print(dmg)
        if len(dmg)==3:
            line = dmg.split('d',-1)
            #print(line)
            try:
                dmg_dices=int(line[0])
                dmg_sides=int(line[1])
                max_dmg = dmg_dices * dmg_sides
                self.__attributes['min_dmg']=dmg_dices
                self.__attributes['max_dmg']=max_dmg
                #print('here we are at the test_me dmg block')
            except Exception:
                self.fail=True
                print('failasi')
        elif len(dmg)==5:
            if dmg.count('+')==1:
                try:
                    line = dmg.split('+', -1)
                    plus_mod = int(line[1])
                    base_damage = line[0].split('d', -1)
                    dmg_dices=int(base_damage[0])
                    dmg_sides=int(base_damage[1])
                    max_dmg = dmg_dices * dmg_sides + plus_mod
                    min_dmg = dmg_dices + plus_mod

                    self.__attributes['min_dmg']=min_dmg
                    self.__attributes['max_dmg']=max_dmg

                except Exception:
                    self.fail = True
            elif dmg.count('-')==1:
                try:
                    line = dmg.split('-', -1)
                    plus_mod = int(line[1])
                    base_damage = line[0].split('d', -1)
                    dmg_dices=int(base_damage[0])
                    dmg_sides=int(base_damage[1])
                    max_dmg = dmg_dices * dmg_sides - plus_mod
                    min_dmg = dmg_dices - plus_mod

                    self.__attributes['min_dmg']=min_dmg
                    self.__attributes['max_dmg']=max_dmg

                except Exception:
                    self.fail = True
        else:
            self.fail=True
    def test_shots(self):
        shots = self.__attributes['Shots']
        try:
            number = int(shots)
        except Exception:
            self.fail = True

    def test_rof(self):
        rof = self.__attributes['ROF']
        try:
            number = int(rof)
        except Exception:
            self.fail = True

    def test_rel(self):
        rel = self.__attributes['Rel']
        text = ''
        if rel == 'UR':
            text = 'Unreliable'
        elif rel == 'ST':
            text = 'Standard'
        elif rel == 'VR':
            text = 'Very reliable'
        else:
            text = 'fail'
            self.fail=True
        self.__attributes['rel_text'] = text

    def test_range(self):
        range = self.__attributes['Range']
        try:
            number = int(range[:-1])
        except Exception:
            self.fail=True

    def test_cost(self):
        cost = self.__attributes['Cost']
        try:
            number = int(cost)
        except Exception:
            self.fail=True

    

    def test_me(self):
        self.fail = False
        try:
            self.test_type()
            self.test_WA()
            self.test_ava()
            self.test_con()
            self.test_dmg()
            self.test_shots()
            self.test_rof()
            self.test_rel()
            self.test_range()
            self.test_cost()
        except Exception:
            print('failed testing')
            self.fail = True

    def addAttribute(self, attribute, value):
        self.__attributes[attribute] = value

    def getAttributes(self):
        return self.__attributes
    
    def getAttribute(self, attribute):
        try:
            return self.__attributes[attribute]
        except Exception:
            return 'fail'
    
    def count_avail_diff(self):
        ava = self.__attributes["Avail"]
        diff = 0
        if ava == 'E':
            diff = 14
        if ava == 'C':
            diff = 18
        if ava == 'P':
            diff = 22
        if ava == 'R':
            diff = 26
        if ava == 'N':
            diff = 30

        self.__attributes["Avail_diff"] = diff

    



