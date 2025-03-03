class Person :
    moods=('happy','tired','lazy')
    def __init__(self,name,money,mood,healthRate):
        self.name=name 
        self.money=money 
        self.mood = mood if mood in self.moods else 'happy'
        if 0<=healthRate and healthRate<=100:
            self.healthRate=healthRate 
        else:
            print("invalied") 

    def sleep(self,hours):
        if hours == 7:
            self.mood='happy'
        elif hours < 7:
            self.mood='tired'
        else :
            self.mood='lazy'

    def eat(self,meals):
        if meals == 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.heathRate ="50%"
        else:
            print("invalied num of meals") 

    def buy(self,items):
        cost = items * 10
        if cost <= self.money:
            self.money -= cost
        else:
            print("the money not enough !")

        
        # return self.__name
    def __str__(self):
        return f"name:{self.name},money:{self.money},healthy:{self.healthRate},mood:{self.mood}"
    

# Person1 =Person('mohamed',10000,'happy',100)
# Person1.sleep(9)
# print(Person1.mood)
# Person1.eat(2)
# print(Person1.healthRate)
# print(Person1.__str__())
        
   