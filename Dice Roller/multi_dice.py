import random
dice_dict = {"D4": 4,"D6": 6,"D8": 8,"D10": 10,"D12":12,"D20":20}
#choose how many dice you want
print(dice_dict.keys())
die_selected = input("What kind of die?: ")

#choose what first die is of __selection__
die_quantity=int(input("How many dice do you want of that type?: "))

#output role (dice_quantity) times
for i in range(0, die_quantity):
    #"generating number"
    landed_number = (random.choice(range(1,(dice_dict.get(die_selected)+1),1)))
    print("You rolled a "+str(landed_number)+ ".")

#Shipping Crate: 
#"
# import random
# dice_dict = {"D4": 4,"D6": 6,"D8": 8,"D10": 10,"D12":12,"D20":20}
# die_selected = input("What kind of die?: ")
# die_quantity = int(input("How many dice do you want of that type?: "))
# for i in range(0, die_quantity):
#    landed_number = (random.choice(range(1,(dice_dict.get(die_selected)+1),1)))
#    print("You rolled a "+str(landed_number))
#"