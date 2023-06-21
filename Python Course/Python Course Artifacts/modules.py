#module = file containing python code
    #used with modular programming (diff python script)
import modules1 

modules1.hello()
modules1.bye()

    
    
from modules1 import hello, bye #could also do import all = *
hello()
bye()

#help("modules") #for all possible modules
