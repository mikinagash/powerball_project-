from class_tballs import Tballs
class Mwp(Tballs):
    power_ball = 0
    whit_balls = 0
    x = Tballs('j').lucky_numbers()
    y = Tballs('k').users_lucky_numbers()
    
    def __init__(self,name):
        super().__init__(name)

    def match(self):
        list1 = self.x[0:5]
        list2 = self.y[0:5]
        self.filterNumbers(list1,list2)

#function that checks several matching numbers and prints a winning amount accordingly
        
    def filterNumbers(self,list1,list2):
        for i in list1:
            for k in list2:
                if i == k:
                 self.whit_balls +=1
        if self.x[-1] == self.y[-1]:
            self.power_ball += 1
        if self.whit_balls == 1  and self.power_ball == 1 or self.whit_balls ==0 and self.power_ball == 1 :
            print("YOU WIN 4$ ")
        elif self.whit_balls == 5 and self.power_ball == 1:
            print("Congratulations ! \nYOU WIN THE BIG PRICE !!! 324,000,000$")
        elif self.whit_balls == 5 and self.power_ball == 0:
            print("YOU WIN 1,000,000$ ")
        elif self.whit_balls == 4 and self.power_ball == 1:
            print("YOU WIN 10,000")
        elif self.whit_balls == 4 and self.power_ball == 0:
            print("YOU WIN 100$")
        elif self.whit_balls == 3 and self.power_ball == 1:
            print("YOU WIN 100$")
        elif self.whit_balls == 3 and self.power_ball == 0:
            print("YOU WIN 7$")
        elif self.whit_balls == 2 and self.power_ball == 1:
            print("YOU WIN 7$")
        else:
            print("TRY AGAIN ")
        print("You have",self.whit_balls,"whit balls" )
        print( "You have ",self.power_ball,"power ball ")












































        # print("Your numbers is:")
        # print(','.join(map(str,super().lucky_numbers())))
        # print("Today numbers:")
        # print(','.join(map(str,super().lucky_numbers())))
        # self.power_ball = 0
        # self.whit_balls = 0
        # list1 = self.lucky_numbers()
        # list2 = self.lucky_numbers()
        # listl = list1[0:5]
        # listu = list2[0:5]
        # for i in list1:
        #     for k in list2:
        #         if i == k:
        #          self.whit_balls +=1
        # if listl[-1] == listu[-1]:
        #     self.power_ball += 1
        # if self.whit_balls == 1  and self.power_ball == 1 or self.whit_balls ==0 and self.power_ball == 1 :
        #     print("YOU WIN 4$ ")
        # elif self.whit_balls == 5 and self.power_ball == 1:
        #     print("Congratulations ! \nYOU WIN THE BIG PRICE !!! 324,000,000$")
        # elif self.whit_balls == 5 and self.power_ball == 0:
        #     print("YOU WIN 1,000,000$ ")
        # elif self.whit_balls == 4 and self.power_ball == 1:
        #     print("YOU WIN 10,000")
        # elif self.whit_balls == 4 and self.power_ball == 0:
        #     print("YOU WIN 100$")
        # elif self.whit_balls == 3 and self.power_ball == 1:
        #     print("YOU WIN 100$")
        # elif self.whit_balls == 3 and self.power_ball == 0:
        #     print("YOU WIN 7$")
        # elif self.whit_balls == 2 and self.power_ball == 1:
        #     print("YOU WIN 7$")
        # else:
        #     print("TRY AGAIN ")
        # print("You have",self.whit_balls,"whit balls" )
        # print( "You have ",self.power_ball,"power ball ")
        #





