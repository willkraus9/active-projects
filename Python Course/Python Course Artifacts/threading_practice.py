#thread in computer engineering: flow of executing instructions
    #each take a turn running due to GIL (1 thread running at one time)

#tasks can either be cpu bound or io bound:
    #cpu bound = program waiting for internal events (better to use multiprocessing)
    #io bound = waiting for external (user input, web scraping, etc.)
        #for this one, use multithreading

import threading
import time

print(threading.active_count())
print(threading.enumerate())
    #can have one thread for input, another for countdown timer

def eat_breakfast():
    time.sleep(3)
    print('You finished breakfast')
def drink_coffee():
    time.sleep(4)
    print('You drink coffee')
def study():
    time.sleep(5)
    print('You finish studying')
    
x = threading.Thread(target = eat_breakfast, args=())
x.start()
y = threading.Thread(target = drink_coffee, args=())
y.start()
z = threading.Thread(target = study, args=())
z.start()

#eat_breakfast()
#drink_coffee()
#study()
