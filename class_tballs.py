from colorama import Fore,Style  #A function that adds color to numbers
from class_game import Game     #name is inherited
import random   #Gives availability to call numbers at random
class Tballs(Game):
    def __init__(self,name):
        super().__init__(name)

# function that pulls 5 numbers + a strong 1 number randomly and puts them in the list of daily lucky numbers
    def lucky_numbers(self):
        numbers = []
        for i in range(5):
            num = random.randint(1, 20)
            while num in numbers:
                num = random.randint(1, 20)
            numbers.append(num)
        todays_lucky_numbers = sorted(numbers)
        power_ball = random.randint(1, 10)
        todays_lucky_numbers.append(power_ball)
        print(Fore.YELLOW,"Today's powerball wining numbers :\n",Fore.MAGENTA, todays_lucky_numbers ,Style.RESET_ALL)
        return todays_lucky_numbers


# function that pulls 5 numbers + a strong 1 number randomly and puts them in the list of the user's lucky numbers
    def users_lucky_numbers(self):
        numbers = []
        for i in range(5):
            num = random.randint(1, 20)
            while num in numbers:
                num = random.randint(1, 20)
            numbers.append(num)
        user_lucky_numbers = sorted(numbers)
        power_ball = random.randint(1, 10)
        user_lucky_numbers.append(power_ball)
        print(Fore.YELLOW,"Your lucky numbers :\n" ,Fore.MAGENTA, user_lucky_numbers,Style.RESET_ALL)
        print("-----------------------")
        return user_lucky_numbers

