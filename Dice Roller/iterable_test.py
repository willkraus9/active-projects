import random
dice_dict = {"D4": 4,"D6": 6,"D8": 8,"D10": 10,"D12":12,"D20":20}
die_selected = input("What kind of die?: ")
die_quantity = int(input("How many dice do you want of that type?: "))
landed_list = []
for i in range(0, die_quantity):
    landed_number = (random.choice(range(1,(dice_dict.get(die_selected)+1),1)))
    #add to landed_number list
    landed_list.append([landed_number])
    #skip to next value in iterable   
print(landed_list) #print second values of all 2D matrices
