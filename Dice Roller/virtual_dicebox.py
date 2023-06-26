import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random
#----------------------------------------------------
#Die roller + interface 
dice_dict = {"D4": 4,"D6": 6,"D8": 8,"D10": 10,"D12":12,"D20":20}
die_selected = input("Of "+str(dice_dict.keys()) +" ,what kind of die are you rolling?: ")
die_quantity = int(input("How many are you rolling of that type?: "))
landed_list = []
for i in range(0, die_quantity):
    landed_number = (random.choice(range(1,(dice_dict.get(die_selected)+1),1)))
    #add to landed_number list
    landed_list.append([landed_number])
    #skip to next value in iterable   
print(landed_list) 
#----------------------------------------------------
#Histogram for dice rolled
data=landed_list
#for testing: data = np.random.randint(1,(dice_dict.get(die_selected)))
heights,bins = np.histogram(data,bins=50)
#Normalize
heights = heights/float(sum(heights))
binMids=bins[:-1]+np.diff(bins)/2.
#formatting gaph
plt.title('Die Results and Probabilities')
plt.xlabel('Landed Dice')
plt.ylabel('Percent dice landed')
plt.grid(True)
plt.axis([1, dice_dict.get(die_selected)+1, 0, 1]) 
plt.plot(binMids,heights)
plt.show() 