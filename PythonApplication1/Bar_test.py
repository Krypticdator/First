from Process import Process
from Process import Character
from dice import Dice

class Bar:
    

    def __init__(self):
        self.__name =""
        self.__staff = []
        self.__owner = Character()
        self.__processes = {}
        self.__hours_open = []
        self.__customers = []
        self.__attributes = {}

        self.__name = "Joes Shithole"
        
        self.__owner.setRandomStats()
        self.__owner.setRandomSkills()

        self.__attributes["popularity"] = 1 #Increases and decreases by every first impression in the bar according to output. 

        self.__attributes["dirtiness"] = 0  #increases by everytime someone cleanes, decreases every hour of customer in the house
                                            #roll 10: improve clean +1, 14: improve clean +2, 18 improve clean +3 and so on.
        self.__attributes["security"] = 0   #Value increases with every security-person and their wpn total damage combined
                                            #Decreases with every visible weapon at customers and their total damage output
        self.__attributes["style"] = 0      #Decorations and mood of the place. permanent value in the place


        self.addProcess("serving", "Human Perception", self.__owner)
        self.addProcess("cleaning", "Cleaning", self.__owner)

        print(self.__processes.values)

        for i in range(0, 23):
            self.__hours_open.append("open")   

    def Operate_hour(self):
        num = self.__attributes["popularity"]
        d = Dice()
        dice = d.Roll(num, 6)

        for i in range(0, dice):
            x = Character()
            x.setRandomStats()
            x.setRandomSkills()
            self.__customers.append(x)
        #print(self.__customers)
        

        for i in range(0, len(self.__customers)):
            self.__processes["serving"].set_difficulty(self.__customers[i].get_skill_throw("Persuasion & Fast Talk"))
            self.__processes["serving"].run_process()
            self.__attributes["dirtiness"] = self.__attributes["dirtiness"] + 1
            resolution = self.__processes["serving"].get_resolution()
            self.__customers[i].setLike(self.__name, resolution)
            print(self.__customers[i].getLike(self.__name))

    def addProcess(self, process_name, req_skill, worker):
        p = Process()
        p.assign_to_taskgroup(worker)
        p.set_req_skills(req_skill)
        print(p._Process__req_skills)

        self.__processes[process_name]=p
        


            