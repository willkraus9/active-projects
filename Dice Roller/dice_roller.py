import random
#DONE stored dictionary of all possible die types
dice_dict = {"D4": 4,"D6": 6,"D8": 8,"D10": 10,"D12":12,"D20":20}

#used for testing:     
die_selected = (input("Input a die: "))

#DONE get number from dice_dict
number_die = (dice_dict.get(die_selected))
#DONE choose a number at random based on die selection
landed_number = (random.choice(range(1,number_die,1)))

#used for testing:
print("You landed a "+str(landed_number))