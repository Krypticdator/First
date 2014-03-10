from item import item
from dice import Dice
class cyberitem(item):
    """description of class"""
    def __init__(self, category="undefined", name="undefined", description_short="undefined",description_long="undefined", operation_diff="undefined", hum_loss="undefined", cost="undefined", req_item_type="body", starter='off'):
        super().__init__()
        self.set_attribute("name", name)
        self.set_attribute("category", category)
        self.set_attribute("description_short", description_short)
        self.set_attribute("description_long", description_long)
        self.set_operation_diff(operation_diff)
        self.set_attribute("hum_loss", hum_loss)
        self.set_attribute('hum_loss_type','damage')
        self.set_hum_loss(hum_loss)
        self.calc_preview_hum_cost()
        self.set_attribute("cost", cost)
        self.test_cost()
        self.set_attribute("req_item", req_item_type)
        self.set_attribute("starter", starter)
        installed_options = []
        self.set_attribute("installed_options", installed_options)
        #self.set_attribute('hum_cost_min', 0)
        #self.set_attribute('hum_cost_max', 0)

    def set_operation_diff(self, operation_diff):
        if operation_diff=='M' or operation_diff=='MA' or operation_diff=='CR' or operation_diff=='N':
            self.set_attribute("operation_diff", operation_diff)
            self.set_attribute("fail", "false")
        else:
            self.set_attribute("fail", "true")

    def add_installed_option(self, cyberitem):
        array = self.get_attribute('installed_options')
        array.append(cyberitem)

    def set_hum_loss(self, hum_loss):
        self.set_attribute('hum_loss_divide', False)
        self.set_attribute('hum_loss_add',False)
        self.set_attribute('hum_dice_count',0)
        self.set_attribute('hum_dice',0)
        if hum_loss.count('-')==1:
            self.set_attribute('hum_loss_type', 'reduce')
            hum_loss = hum_loss[1:]
        if len(hum_loss)==5:
            if hum_loss.count('/')==1:
                #print("must divide!")
                self.set_attribute('hum_loss_divide', True)
                line = hum_loss.split('/',-1)
                self.set_attribute('hum_loss_divide_num',int(line[1]))
                line2=line[0].split('d',-1)
                self.set_attribute('hum_dice_count',int(line2[0]))
                self.set_attribute('hum_dice', int(line2[1]))
            elif hum_loss.count('+')==1:
                self.set_attribute('hum_loss_add', True)
                line = hum_loss.split('+', -1)
                self.set_attribute('hum_loss_add_num', int(line[1]))
                line2=line[0].split('d',-1)
                self.set_attribute('hum_dice_count',int(line2[0]))
                self.set_attribute('hum_dice',int(line2[1]))
        elif len(hum_loss)==3:
            line = hum_loss.split('d', -1)
            self.set_attribute('hum_dice_count', int(line[0]))
            self.set_attribute('hum_dice', int(line[1]))
        elif len(hum_loss)==2:
            if hum_loss =='.5':
                self.set_attribute('hum_loss_type', 'half')
                self.set_attribute('hum_dice_count', 1)
                self.set_attribute('hum_dice', 1)
        elif len(hum_loss)==1:
            try:
                cost = int(hum_loss)
                self.set_attribute('hum_dice_count', cost)
                self.set_attribute('hum_dice', 1)
            except Exception:
                cost = 0
                self.set_attribute('hum_dice_count', cost)
                self.set_attribute('hum_dice', 1)

    def test_cost(self):
        cost = self.get_attribute('cost')
        if cost.count('-')==1:
            line = cost.split('-', -1)
            cost = line[1]
            self.set_attribute('cost',cost)

    def calc_effective_hum_cost(self):
        #print('calc_effective_hum_cost funkt')
        sides=self.get_attribute('hum_dice_count')
        dice =self.get_attribute('hum_dice')
        add = self.get_attribute('hum_loss_add')
        divide = self.get_attribute('hum_loss_divide')
        final_hum_cost=0
        add_num=0
        divide_num=1
        zeroes = False
        if sides==0 or dice==0:
           zeroes=True
           #print('zeroes are true')
        if add:
            add_num=self.get_attribute('hum_loss_add_num')
        if divide:
            divide_num = self.get_attribute('hum_loss_divide_num')
        d = Dice()
        if zeroes==True:
            pass
        else:
            #print('zeroes else statement')
            roll = d.Roll(sides, dice)
            final_hum_cost = roll + add_num / divide_num
        if self.get_attribute('hum_loss_type')=='half':
            final_hum_cost = 0.5
        if self.get_attribute("hum_loss_type")=="reduce":
            final_hum_cost = final_hum_cost * -1
        self.set_attribute('effective_hum_cost', final_hum_cost)
        return final_hum_cost

    def calc_preview_hum_cost(self):
        sides=self.get_attribute('hum_dice_count')
        dice =self.get_attribute('hum_dice')
        add = self.get_attribute('hum_loss_add')
        divide = self.get_attribute('hum_loss_divide')
        add_num=0
        divide_num=1
        if sides==0 or dice==0:
            self.set_attribute('hum_cost_min', 0)
            self.set_attribute('hum_cost_max', 0)
            return 0
        if add:
            add_num=self.get_attribute('hum_loss_add_num')
        if divide:
            divide_num = self.get_attribute('hum_loss_divide_num')

        min_dgm = sides + add_num / divide_num
        max_dmg = sides * dice + add_num / divide_num

        if self.get_attribute("hum_loss_type")=="reduce":
            min_dgm = min_dgm * -1
            max_dmg = max_dmg * -1
        if self.get_attribute('hum_loss_type')=='half':
            min_dgm = 0.5
            max_dmg = 0.5
            

        self.set_attribute('hum_cost_min', min_dgm)
        self.set_attribute('hum_cost_max', max_dmg)





    

