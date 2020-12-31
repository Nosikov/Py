class Hero():
    """Class of our Game"""
    def __init__(self,name,level,race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        discription =(self.name +" level is "+str(self.level))
        print(discription)
    def level_up(self):
        self.level+=1
    def move(self):
        print("hero "+self.name +"start move...")
#---------------
class SuperHero(Hero):
    def __init__(self,name,level,race, magiclevel):
        super().__init__(name,level,race)
        self.magiclevel = magiclevel
        self.magic=100
    def makemagic(self):
        self.magic-=10

    def show_hero(self):
        discription =(self.name +" level is "+str(self.level) +"level magic=" + str(self.magic))
        print(discription)

