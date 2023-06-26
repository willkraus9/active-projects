import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#----------------------------------------------------
#TODO distribution curves for each value

#select die
dice_dict = {"D4": 4,"D6": 6,"D8": 8,"D10": 10,"D12":12,"D20":20}
die_selected = input("What kind of die?: ")

data = np.random.rand(1000)
# https://stackoverflow.com/questions/30889444/python-matplotlib-probability-mass-function-as-histogram
heights,bins = np.histogram(data,bins=50)
heights = heights/(sum(heights))
binMids=bins[:-1]+np.diff(bins)/2.
plt.plot(binMids,heights)

fig,ax = plt.subplots(figsize =(5,2.7), layout = 'constrained')
n, bins, patches = ax.hist(data,100,density = True, facecolor = 'C0')
ax.axis([0, dice_dict.get(die_selected)+3, 0, 0.5]) #will have to replace 2nd later with max_roll variable, 4th with highest_probability
plt.show()
#TODO
# get graphs for each type of die
# add the graphs together 

# landed_list add values at end together
# also add different types of dice together (a D6 and a D10)

